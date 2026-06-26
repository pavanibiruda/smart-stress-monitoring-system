import tensorflow as tf

model = tf.keras.models.load_model(
    "models/resnet50_emotion_model.keras"
)

converter = tf.lite.TFLiteConverter.from_keras_model(model)

converter.optimizations = [tf.lite.Optimize.DEFAULT]

tflite_model = converter.convert()

with open("emotion_model_quant.tflite", "wb") as f:
    f.write(tflite_model)

print("Quantized TFLite model created successfully")