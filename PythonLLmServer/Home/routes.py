#!/usr/bin/env python3 

# Importing the necessary modules 
import os 
import ollama
import base64
from flask import request, jsonify, Blueprint, render_template

# Creating the blueprint object 
home = Blueprint('home', __name__, 
                 template_folder='templates', 
                 static_folder='static')


# Creating a route for the home page 
@home.route('/', methods=['GET', 'POST'])
def Home(): 
    # Rendering the home page 
    return render_template('home.html')


# Creating a route for handling llama request 
@home.route('/llm-request', methods=['POST'])
def LlmRequest(): 
    # Getting the user's message 
    requestData = request.get_json() 
    usersMessage = requestData["message"]

    # Using try and execpt block 
    try: 
        # Sending the users message into the llama3 model 
        response = ollama.chat(model="llama3.2:1b", messages=[
            {'role': 'user', 'content': usersMessage}
        ])

        # Getting the message 
        responseMessage = response['message']['content']; 

        # Sending back the message 
        return jsonify({
            "status": "success", 
            "message": responseMessage, 
            "statusCode": 200
        })

    except Exception as e: 
        return jsonify({
            "status": "error", 
            "message": str(e), 
            "statusCode": 404
        })
    

# Creating a route for analyzing an image 
@home.route('/analyze-image', methods=['POST'])
def AnalyzeImage(): 
    # Checking if an image file is sent in the request 
    if 'image' not in request.files: 
        return jsonify({
            "status": "error", 
            "message": "No image file provided", 
            "statusCode": 400
        })
    
    # Getting the image file 
    imageFile = request.files['image']

    # Saving the image temporarily 
    uploadDir = os.path.join("Home", "static", "uploads")
    imagePath = os.path.join(uploadDir, imageFile.filename)
    
    # Saving the image 
    imageFile.save(imagePath) 

    # using try catch block 
    try:
        # Sending the image to the Ollama model for analysis
        response = ollama.chat(model="llama3.2:1b", messages=[
            {'role': 'user', 
                'content': 'Analyze this image', 
                'images': [imagePath]
            }
        ])

        # Getting the response message 
        responseMessage = response['message']['content']

        # Sending back the response 
        return jsonify({
            "status": "success", 
            "message": responseMessage, 
            "statusCode": 200
        })

    except Exception as e: 
        return jsonify({
            "status": "error", 
            "message": str(e), 
            "statusCode": 500
        })
    
    # # 
    # finally: 
    #     # 
    #     if os.path.exists(imagePath): 
    #         os.remove(imagePath)



