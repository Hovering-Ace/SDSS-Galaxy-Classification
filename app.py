# this commentesd code is used when the model in same folder but,
# due to large size it cnnot be uploaded on github so, second code is 
# modified to download model fron drive in realtime and use it in render.

# from flask import Flask, render_template, request
# import joblib
# import numpy as np
# import requests
# import pickle
# import os

# # URL where the model is stored (Replace with your cloud link)
# MODEL_URL = "https://drive.google.com/uc?export=download&id=YOUR_FILE_ID"

# MODEL_PATH = "model/random_forest_model.pkl"

# # Function to download model if not found locally
# def download_model():
#     if not os.path.exists(MODEL_PATH):
#         print("Downloading model...")
#         response = requests.get(MODEL_URL)
#         with open(MODEL_PATH, "wb") as file:
#             file.write(response.content)
#         print("Model downloaded successfully!")

# # Call this function before loading the model
# download_model()

# # Load the model
# with open(MODEL_PATH, "rb") as model_file:
#     model = pickle.load(model_file)


# app = Flask(__name__)

# # Load the trained model
# model = joblib.load('random_forest_model.pkl')

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     try:
#         input_data = [float(x) for x in request.form.values()]
#         input_array = np.array(input_data).reshape(1, -1)
#         prediction = model.predict(input_array)[0]
        
#         return render_template('output.html', prediction=prediction)
#     except Exception as e:
#         return f"Error: {str(e)}"

# if __name__ == '__main__':
#     app.run(debug=True)

# --------------  code 2 -----------

from flask import Flask, render_template, request
import numpy as np
import requests
import pickle
import os

# URL where the model is stored (Replace with your Google Drive link)
MODEL_URL = "https://drive.google.com/uc?export=download&id=1P2IFlzyTBNtJuvbQjAGm86w8P2aUAWB6"


MODEL_PATH = "model/random_forest_model.pkl"

# Function to download model if not found locally
def download_model():
    if not os.path.exists(MODEL_PATH):
        print("Downloading model...")
        os.makedirs("model", exist_ok=True)  # Ensure the model folder exists
        response = requests.get(MODEL_URL)
        with open(MODEL_PATH, "wb") as file:
            file.write(response.content)
        print("Model downloaded successfully!")

# Call this function before loading the model
download_model()

# Load the model
with open(MODEL_PATH, "rb") as model_file:
    model = pickle.load(model_file)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        input_data = [float(x) for x in request.form.values()]
        input_array = np.array(input_data).reshape(1, -1)
        prediction = model.predict(input_array)[0]
        
        return render_template('output.html', prediction=prediction)
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
