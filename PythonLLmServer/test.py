import ollama
import os 
import base64

# 
uploadDir = os.path.join("Home", "static", "uploads")
imagePath = os.path.join(uploadDir, "image.jpg")

#
# response = ollama.chat(model="llama3.2:1b", messages=[
#     {'role': 'user', 
#         'content': 'Analyze this image', 
#         'images': imagePath
#     }
# ])

# Sending the base64 image to the Ollama model for analysis
response = ollama.chat(model="llama3.2:1b", messages=[
    {'role': 'user', 'content': 'Describe this image', 'images': ['./image.jpg']}
])

print(response['message']['content'])