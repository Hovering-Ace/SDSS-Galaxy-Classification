from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model
model = joblib.load('random_forest_model.pkl')

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
