from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

# Load the model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return render_template('index2.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Define 'data' without missing features
    data = [
        float(request.form.get('time_in_hospital')),
        float(request.form.get('num_lab_procedures')),
        float(request.form.get('num_procedures')),
        float(request.form.get('num_medications')),
        float(request.form.get('number_outpatient')),
        float(request.form.get('number_emergency')),
        float(request.form.get('number_inpatient')),
        float(request.form.get('number_diagnoses'))
        
    ]

    # Make prediction
    prediction = model.predict([data])[0]
    
    # Return the result
    result = "High risk of readmission" if prediction == 1 else "Low risk of readmission"
    return render_template('index2.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)
