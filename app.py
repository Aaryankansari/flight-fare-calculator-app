from flask import Flask, request, render_template, url_for
from flask_cors import cross_origin
import sklearn
import pandas as pd
import joblib
import pickle

app = Flask(__name__)

# Load the trained model and feature columns
model = joblib.load('flight_fare_model.pkl')
model_columns = joblib.load('model_columns.pkl')

@app.route("/")
@cross_origin()
def home():
    return render_template("index.html")

@app.route("/predict", methods=["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":
        # Date_of_Journey
        date_dep = request.form["Dep_Time"]
        Journey_day = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").day)
        Journey_month = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").month)

        # Departure
        Dep_hour = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").hour)
        Dep_min = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").minute)

        # Arrival
        date_arr = request.form["Arrival_Time"]
        Arrival_hour = int(pd.to_datetime(date_arr, format="%Y-%m-%dT%H:%M").hour)
        Arrival_min = int(pd.to_datetime(date_arr, format="%Y-%m-%dT%H:%M").minute)

        # Duration
        dur_hour = abs(Arrival_hour - Dep_hour)
        dur_min = abs(Arrival_min - Dep_min)

        # Total Stops
        Total_Stops = int(request.form["stops"])

        # Airline
        airline = request.form['airline']
        
        # Source
        Source = request.form["Source"]
        
        # Destination
        Destination = request.form["Destination"]

        # Create a dataframe for the input data with the same columns as training data
        input_data = pd.DataFrame(columns=model_columns)
        
        # Initialize with zeros
        input_data.loc[0] = 0
        
        # Set values
        input_data.at[0, 'Total_Stops'] = Total_Stops
        input_data.at[0, 'Journey_day'] = Journey_day
        input_data.at[0, 'Journey_month'] = Journey_month
        input_data.at[0, 'Dep_hour'] = Dep_hour
        input_data.at[0, 'Dep_min'] = Dep_min
        input_data.at[0, 'Arrival_hour'] = Arrival_hour
        input_data.at[0, 'Arrival_min'] = Arrival_min
        input_data.at[0, 'Duration_hours'] = dur_hour
        input_data.at[0, 'Duration_mins'] = dur_min

        # One-hot encoding manual setting
        if 'Airline_' + airline in input_data.columns:
            input_data.at[0, 'Airline_' + airline] = 1
            
        if 'Source_' + Source in input_data.columns:
            input_data.at[0, 'Source_' + Source] = 1
            
        if 'Destination_' + Destination in input_data.columns:
             input_data.at[0, 'Destination_' + Destination] = 1
        
        prediction = model.predict(input_data)
        output = round(prediction[0], 2)

        return render_template('result.html', prediction_text="Your Flight price is Rs. {}".format(output))

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
