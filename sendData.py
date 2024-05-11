import os
import random
import requests
import json

# API endpoint
api_url = "https://alnp8uiudi.execute-api.us-east-2.amazonaws.com/secondStage/sendData"

# Get list of CSV files in the current directory
csv_files = [file for file in os.listdir() if file.endswith(".csv")]

# Choose a random CSV file
random_csv_file = random.choice(csv_files)

# Read contents of the chosen CSV file
with open(random_csv_file, "r") as file:
    csv_contents = file.read()

# Prepare JSON request body with CSV contents
request_body = {
    "csv_content": csv_contents
}

# print(request_body)

# Make POST request to the API endpoint
response = requests.post(api_url, json=request_body)

# Check if request was successful
if response.status_code == 200:
    print("POST request successful.")
    print("Response:", response.json())
else:
    print("Error:", response.status_code)
    print("Response:", response.text)
