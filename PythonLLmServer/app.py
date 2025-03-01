#!/usr/bin/env python3 

# importing the necessary modules 
import os 
from flask import Flask
from flask_cors import CORS 
from datetime import timedelta
from dotenv import load_dotenv

# loading the env 
load_dotenv() 

# importing the views 
from Home.routes import home

# Creating the flask application 
app = Flask(__name__, 
            static_folder=None, 
            template_folder=None)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0 
app.secret_key = os.getenv('SECRET_KEY')


# Setting the cors application 
CORS(app)

# Register the views 
app.register_blueprint(home, url_prefix="/")

# Running the flask application 
if __name__ == "__main__": 
    app.run(port=3001, host="localhost", debug=True)
    app.run() 