from flask import Flask, render_template, Response, jsonify, request

import cv2
import numpy as np
import tensorflow as tf

from tensorflow.keras.applications.resnet50 import preprocess_input

import random
import os
import base64
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

MODEL_PATH = "models/resnet50_emotion_model.keras"

emotion_labels = [
    "Angry",
    "Disgust",
    "Fear",
    "Happy",
    "Neutral",
    "Sad",
    "Surprise"
]

model = None

if os.path.exists(MODEL_PATH):
    model = tf.keras.models.load_model(MODEL_PATH)
    print("ResNet50 emotion model loaded successfully")
    print("Model input shape:", model.input_shape)
else:
    print("Model not found:", MODEL_PATH)

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="pavani@123",
    database="smart_stress_db"
)

cursor = db.cursor(dictionary=True)

latest_data = {
    "emotion": "Detecting...",
    "heartRate": "Detecting...",
    "respRate": "Detecting...",
    "blinkRate": "Detecting...",
    "bp": "Detecting...",
    "status": "Ready"
}


def predict_emotion(face):

    try:
        face = cv2.resize(face, (224,224))

        face = cv2.cvtColor(
            face,
            cv2.COLOR_BGR2RGB
        )

        face = np.expand_dims(face, axis=0)

        face = preprocess_input(face)

        prediction = model.predict(
            face,
            verbose=0
        )

        index = np.argmax(prediction)

        emotion = emotion_labels[index]

        print(
            "Detected Emotion:",
            emotion,
            "Confidence:",
            np.max(prediction)
        )

        return emotion


    except Exception as e:

        print("Prediction Error:",e)

        return "PREDICT_ERROR"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/facescan")
def facescan():
    return render_template("facescan.html")


@app.route("/questionnaire")
def questionnaire():
    return render_template("questionnaire.html")


@app.route("/reports")
def reports():
    return render_template("reports.html")


@app.route("/recommendations")
def recommendations():
    return render_template("recommendations.html")


@app.route("/history")
def history():
    return render_template("history.html")


@app.route("/profile")
def profile():
    return render_template("profile.html")


@app.route("/api/register", methods=["POST"])
def api_register():
    try:
        data = request.get_json()

        username = data["username"]
        email = data["email"]
        occupation = data["occupation"]
        password = generate_password_hash(data["password"])

        cursor.execute(
            """
            INSERT INTO users 
            (username, email, occupation, password) 
            VALUES (%s, %s, %s, %s)
            """,
            (username, email, occupation, password)
        )

        db.commit()

        return jsonify({"success": True})

    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        })



@app.route("/api/login", methods=["POST"])
def api_login():
    try:
        data = request.get_json()

        username = data["username"]
        occupation = data["occupation"]
        password = data["password"]

        cursor.execute(
            """
            SELECT * FROM users 
            WHERE username=%s AND occupation=%s
            """,
            (username, occupation)
        )

        user = cursor.fetchone()

        if user and check_password_hash(user["password"], password):
            return jsonify({
                "success": True,
                "user_id": user["user_id"],
                "username": user["username"],
                "email": user["email"],
                "occupation": user["occupation"]
            })

        return jsonify({
            "success": False,
            "error": "Invalid username, occupation or password"
        })

    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        })


@app.route("/api/forgot_password", methods=["POST"])
def forgot_password():
    try:
        data = request.get_json()

        username = data["username"].strip()
        email = data["email"].strip()
        new_password = generate_password_hash(data["newPassword"])

        cursor.execute(
            "SELECT user_id FROM users WHERE username=%s AND email=%s",
            (username, email)
        )

        user = cursor.fetchone()

        if user is None:
            return jsonify({
                "success": False,
                "error": "Username and email do not match"
            })

        cursor.execute(
            "UPDATE users SET password=%s WHERE user_id=%s",
            (new_password, user["user_id"])
        )

        db.commit()

        return jsonify({
            "success": True,
            "message": "Password reset successful"
        })

    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        })

@app.route("/api/verify_user", methods=["POST"])
def verify_user():
    try:
        data = request.get_json()

        username = data["username"].strip()
        email = data["email"].strip()

        cursor.execute(
            "SELECT user_id FROM users WHERE username=%s AND email=%s",
            (username, email)
        )

        user = cursor.fetchone()

        if user is None:
            return jsonify({
                "success": False,
                "error": "Username and email do not match"
            })

        return jsonify({
            "success": True
        })

    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        })

@app.route("/analyze_frame", methods=["POST"])
def analyze_frame():
    global latest_data

    try:
        data = request.get_json()

        if not data or "image" not in data:
            return jsonify({
                "success": False,
                "error": "No image received"
            })

        image_data = data["image"]

        if "," in image_data:
            image_data = image_data.split(",")[1]

        image_bytes = base64.b64decode(image_data)

        np_arr = np.frombuffer(image_bytes, np.uint8)

        frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

        if frame is None:
            return jsonify({
                "success": False,
                "error": "Invalid image frame"
            })

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(80, 80)
        )

        if len(faces) == 0:
            return jsonify({
                "success": False,
                "error": "No face detected"
            })

        x, y, w, h = faces[0]

        face = frame[y:y+h, x:x+w]

        emotion = predict_emotion(face)

        if emotion in ["MODEL_NOT_LOADED", "PREDICT_ERROR"]:
            return jsonify({
                "success": False,
                "error": emotion
            })

        heart_rate = random.randint(70, 95)
        resp_rate = random.randint(14, 20)
        blink_rate = random.choice([5, 6, 7, 8, 9, 10])
        systolic = random.randint(110, 125)
        diastolic = random.randint(70, 82)

        bp = f"{systolic}/{diastolic}"

        latest_data = {
            "emotion": emotion,
            "heartRate": heart_rate,
            "respRate": resp_rate,
            "blinkRate": blink_rate,
            "bp": bp,
            "status": "Completed"
        }

        return jsonify({
            "success": True,
            "emotion": emotion,
            "heartRate": heart_rate,
            "respRate": resp_rate,
            "blinkRate": blink_rate,
            "bp": bp
        })

    except Exception as e:
        print("Analyze Frame Error:", e)

        return jsonify({
            "success": False,
            "error": str(e)
        })


@app.route("/api/save_assessment", methods=["POST"])
def save_assessment():
    try:
        data = request.get_json()

        cursor.execute(
            """
            INSERT INTO assessments
            (user_id, emotion, heart_rate, blink_rate, resp_rate,
            blood_pressure, face_score, questionnaire_score,
            final_score, stress_level)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """,
            (
                data["user_id"],
                data["emotion"],
                data["heartRate"],
                data["blinkRate"],
                data["respRate"],
                data["bp"],
                data["faceScore"],
                data["questionnaireScore"],
                data["finalScore"],
                data["stressLevel"]
            )
        )

        db.commit()

        return jsonify({"success": True})

    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        })

@app.route("/api/get_profile/<int:user_id>")
def get_profile(user_id):
    try:
        cursor.execute(
            """
            SELECT 
            user_id,
            username,
            email,
            occupation,
            created_at
            FROM users
            WHERE user_id=%s
            """,
            (user_id,)
        )

        user = cursor.fetchone()

        if user:
            return jsonify({
                "success": True,
                "user": user
            })

        return jsonify({
            "success": False,
            "error": "User not found"
        })

    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        })

@app.route("/api/update_profile/<int:user_id>", methods=["POST"])
def update_profile(user_id):
    try:
        data = request.get_json()

        username = data["username"]
        email = data["email"]

        cursor.execute(
            """
            UPDATE users
            SET username=%s, email=%s
            WHERE user_id=%s
            """,
            (username, email, user_id)
        )

        db.commit()

        return jsonify({"success": True})

    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        })

@app.route("/api/get_reports/<int:user_id>", methods=["GET"])
def get_reports(user_id):
    try:
        cursor.execute(
            """
            SELECT 
                assessment_id,
                emotion,
                heart_rate,
                blink_rate,
                resp_rate,
                blood_pressure,
                face_score,
                questionnaire_score,
                final_score,
                stress_level,
                created_at
            FROM assessments
            WHERE user_id = %s
            ORDER BY created_at DESC
            """,
            (user_id,)
        )

        reports = cursor.fetchall()

        return jsonify({
            "success": True,
            "reports": reports
        })

    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        })

@app.route("/data")
def data():
    return jsonify(latest_data)


if __name__ == "__main__":
    app.run(debug=True)