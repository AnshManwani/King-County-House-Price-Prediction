from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
with open('house_price_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Static mapping from human-readable location to (zipcode, lat, long)
location_data = {
    "Seattle Downtown": (98101, 47.6101, -122.3344),
    "Redmond": (98052, 47.6739, -122.1215),
    "Bellevue": (98004, 47.6104, -122.2007),
    "Kirkland": (98033, 47.6815, -122.2087),
    "Renton": (98057, 47.4829, -122.2171),
    "Kent": (98030, 47.3811, -122.2348),
    "Auburn": (98002, 47.3073, -122.2285),
    "Issaquah": (98027, 47.5301, -122.0326),
    "Federal Way": (98003, 47.3223, -122.3126),
    "Sammamish": (98074, 47.6163, -122.0356),
    # Add more locations here as needed
}

@app.route('/')
def home():
    return render_template('index.html', locations=list(location_data.keys()))

@app.route('/predict', methods=['POST'])
def predict():
    try:
        location_name = request.form['location']
        zipcode, lat, long = location_data.get(location_name, (0, 0.0, 0.0))

        features = [
            float(request.form['bedrooms']),
            float(request.form['bathrooms']),
            float(request.form['sqft_living']),
            float(request.form['sqft_lot']),
            float(request.form['floors']),
            float(request.form['waterfront']),
            float(request.form['view']),
            float(request.form['condition']),
            float(request.form['grade']),
            float(request.form['sqft_above']),
            float(request.form['sqft_basement']),
            float(request.form['yr_built']),
            zipcode,  # replaced year_renovated with zipcode
            lat,
            long
        ]

        prediction = model.predict([np.array(features)])[0]
        prediction = round(prediction, 2)
        return render_template('index.html', prediction_text=f'Estimated Price: ${prediction:,}', locations=list(location_data.keys()), selected_location=location_name)
    except Exception as e:
        return render_template('index.html', prediction_text=f'Error: {str(e)}', locations=list(location_data.keys()))

if __name__ == '__main__':
    app.run(debug=True)
