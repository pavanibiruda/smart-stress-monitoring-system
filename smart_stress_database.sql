CREATE DATABASE smart_stress_db;
 
USE smart_stress_db;
 
 CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    password VARCHAR(255),
    age INT,
    occupation VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE assessments (
    assessment_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    emotion VARCHAR(50),
    heart_rate INT,
    blink_rate INT,
    resp_rate INT,
    blood_pressure VARCHAR(20),
    face_score INT,
    questionnaire_score INT,
    final_score INT,
    stress_level VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

DROP DATABASE smart_stress_db;

DROP TABLE assessments;

DROP TABLE users;

SHOW DATABASES;

SHOW TABLES;

SELECT * FROM users;

SELECT * FROM assessments;

SELECT COUNT(*) FROM users;

SELECT user_id, username, email FROM users;