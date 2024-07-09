from dotenv import load_dotenv
import requests
import os

load_dotenv()

EXTRACT_URI = os.getenv("EXTRACT_URI")

def get_api_response(file):
    response = response = requests.post(
        EXTRACT_URI,
        files={"file": (file.name, file, 'multipart/form-data')}
    )
    return response.json()