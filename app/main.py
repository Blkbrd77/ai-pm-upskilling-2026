"""
Project Health Predictor - Flask Web Application

This app integrates trained ML models to provide project health predictions.
Developed as part of the AI/PM Upskilling Portfolio 2026.

Author: Jay Samples
"""

from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np
import os

app = Flask(__name__)

# Model path - will be populated after training
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'models', 'model.pkl')


def load_model():
    """Load the trained model if it exists."""
    if os.path.exists(MODEL_PATH):
        return joblib.load(MODEL_PATH)
    return None


@app.route('/')
def home():
    """Render the home page with prediction form."""
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    """Handle prediction requests."""
    try:
        model = load_model()

        if model is None:
            return render_template('index.html',
                                   error="Model not yet trained. Complete Phase 2 first!")

        # Extract features from form
        # TODO: Update these based on your final model features
        planned_bac = float(request.form.get('planned_bac', 0))
        time_elapsed = float(request.form.get('time_elapsed', 0))
        hours_logged = float(request.form.get('hours_logged', 0))
        schedule_variance = float(request.form.get('schedule_variance', 0))

        # Prepare features for prediction
        features = np.array([[planned_bac, time_elapsed, hours_logged, schedule_variance]])

        # Make prediction
        prediction = model.predict(features)[0]

        # Format result
        result = {
            'prediction': round(prediction, 2),
            'interpretation': interpret_prediction(prediction),
            'features': {
                'Planned BAC': planned_bac,
                'Time Elapsed (%)': time_elapsed,
                'Hours Logged': hours_logged,
                'Schedule Variance': schedule_variance
            }
        }

        return render_template('index.html', result=result)

    except Exception as e:
        return render_template('index.html', error=str(e))


def interpret_prediction(value):
    """Provide interpretation of the prediction value."""
    # TODO: Customize based on your model's output
    if value < 0:
        return "Project is under budget - performing well!"
    elif value < 10:
        return "Minor cost overrun expected - monitor closely."
    elif value < 25:
        return "Moderate cost overrun - consider corrective actions."
    else:
        return "Significant cost overrun risk - immediate attention required!"


@app.route('/health')
def health():
    """Health check endpoint."""
    return jsonify({'status': 'healthy', 'model_loaded': os.path.exists(MODEL_PATH)})


if __name__ == '__main__':
    app.run(debug=True, port=5000)
