# Project 3 – Serverless Contact Form

## 🎯 Objective
A modern, fully serverless web app that collects contact form submissions and stores them in a secure DynamoDB table via AWS Lambda and API Gateway.

## 🛠 Tools Used
- HTML & CSS
- JavaScript (Fetch API)
- AWS Lambda (Python 3.13)
- API Gateway (HTTP API)
- CloudWatch Logs
- DynamoDB

## 🚀 Live Demo
*Hosted locally*
![Preview](../images/project-3.png)
![Preview](../images/project-3%20logs.png)
![Preview](../images/project-3%20DynamoDB.png)

## 📹 Video explanation
[Click here to view the screen recording](https://drive.google.com/file/d/1g9lIXahdJQWtLl6I5wSSZ9b1gqjwItbv/view?usp=sharing)

## ✅ How It Works
- The user submits a form
- JavaScript sends the data to API Gateway
- API Gateway triggers a Lambda function
- Lambda processes and stores the message in DynamoDB
- Success message appears in the UI

## 🧠 What I Learned
- Built a secure, scalable, and production-style app using 100% managed AWS services
- Understood how to integrate API Gateway + Lambda + DynamoDB
- Using CORS properly

## 🖥 Lambda Backend
See the full Lambda function here: [`lambda_function.py`](./lambda_function.py)
