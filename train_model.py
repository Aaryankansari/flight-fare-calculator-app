import pandas as pd
import numpy as np
import argparse
import sys
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
import joblib
import random
from datetime import datetime, timedelta

def generate_synthetic_data(num_samples=1000):
    """
    Generates a synthetic dataset for flight fare prediction.
    """
    airlines = ['Jet Airways', 'IndiGo', 'Air India', 'Multiple carriers', 'SpiceJet', 'Vistara', 'Air Asia', 'GoAir']
    sources = ['Delhi', 'Kolkata', 'Bangalore', 'Mumbai', 'Chennai']
    destinations = ['Cochin', 'Bangalore', 'Delhi', 'New Delhi', 'Hyderabad', 'Kolkata']
    
    data = []
    
    for _ in range(num_samples):
        airline = random.choice(airlines)
        source = random.choice(sources)
        destination = random.choice([d for d in destinations if d != source])
        
        # Date of Journey
        start_date = datetime.now()
        journey_date = start_date + timedelta(days=random.randint(1, 60))
        date_of_journey = journey_date.strftime("%d/%m/%Y")
        
        # Departure Time
        dep_hour = random.randint(0, 23)
        dep_min = random.choice([0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55])
        dep_time = f"{dep_hour:02d}:{dep_min:02d}"
        
        # Duration
        duration_hours = random.randint(1, 20)
        duration_mins = random.choice([0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55])
        
        # Arrival Time (Simple logic: Dep + Duration)
        arrival_time_obj = datetime.strptime(dep_time, "%H:%M") + timedelta(hours=duration_hours, minutes=duration_mins)
        arrival_time = arrival_time_obj.strftime("%H:%M")
        
        # Total Stops
        total_stops = random.choice(['non-stop', '1 stop', '2 stops', '3 stops', '4 stops'])
        
        # Additional Info
        additional_info = random.choice(['No info', 'In-flight meal not included', 'No check-in baggage included'])
        
        # Price Calculation Logic (Synthetic)
        base_price = 5000
        airline_factor = {'Jet Airways': 1.5, 'IndiGo': 1.0, 'Air India': 1.2, 'Multiple carriers': 1.3, 'SpiceJet': 0.8, 'Vistara': 1.4, 'Air Asia': 0.7, 'GoAir': 0.9}
        source_factor = {'Delhi': 1.2, 'Kolkata': 1.0, 'Bangalore': 1.1, 'Mumbai': 1.3, 'Chennai': 1.0}
        stop_factor = {'non-stop': 1.0, '1 stop': 1.3, '2 stops': 1.6, '3 stops': 1.9, '4 stops': 2.2}
        
        price = base_price * airline_factor[airline] * source_factor[source] * stop_factor[total_stops]
        price += duration_hours * 100 # Long flights cost more
        
        # Random fluctuation
        price = price * random.uniform(0.8, 1.2)
        
        data.append([airline, date_of_journey, source, destination, dep_time, arrival_time, duration_hours, duration_mins, total_stops, additional_info, int(price)])
        
    columns = ['Airline', 'Date_of_Journey', 'Source', 'Destination', 'Dep_Time', 'Arrival_Time', 'Duration_hours', 'Duration_mins', 'Total_Stops', 'Additional_Info', 'Price']
    df = pd.DataFrame(data, columns=columns)
    return df

def train_model():
    print("Generating synthetic data...")
    train_data = generate_synthetic_data(num_samples=2000)
    
    print("Preprocessing data...")
    train_data.dropna(inplace=True)
    
    train_data["Journey_day"] = pd.to_datetime(train_data.Date_of_Journey, format="%d/%m/%Y").dt.day
    train_data["Journey_month"] = pd.to_datetime(train_data.Date_of_Journey, format="%d/%m/%Y").dt.month
    train_data.drop(["Date_of_Journey"], axis=1, inplace=True)

    train_data["Dep_hour"] = pd.to_datetime(train_data["Dep_Time"]).dt.hour
    train_data["Dep_min"] = pd.to_datetime(train_data["Dep_Time"]).dt.minute
    train_data.drop(["Dep_Time"], axis=1, inplace=True)

    train_data["Arrival_hour"] = pd.to_datetime(train_data.Arrival_Time).dt.hour
    train_data["Arrival_min"] = pd.to_datetime(train_data.Arrival_Time).dt.minute
    train_data.drop(["Arrival_Time"], axis=1, inplace=True)
    
    # Handling Categorical Data
    # Airline
    Airline = train_data[["Airline"]]
    Airline = pd.get_dummies(Airline, drop_first=True)
    
    # Source
    Source = train_data[["Source"]]
    Source = pd.get_dummies(Source, drop_first=True)
    
    # Destination
    Destination = train_data[["Destination"]]
    Destination = pd.get_dummies(Destination, drop_first=True)
    
    # Total_Stops
    train_data.replace({"non-stop": 0, "1 stop": 1, "2 stops": 2, "3 stops": 3, "4 stops": 4}, inplace=True)
    
    # Concatenate dataframe
    data_train = pd.concat([train_data, Airline, Source, Destination], axis=1)
    data_train.drop(["Airline", "Source", "Destination", "Additional_Info"], axis=1, inplace=True)
    
    X = data_train.drop('Price', axis=1)
    y = data_train['Price']
    
    # Save column names for prediction
    feature_columns = X.columns.tolist()
    
    print("Training model...")
    reg_rf = RandomForestRegressor()
    reg_rf.fit(X, y)
    
    print("Saving model and columns...")
    joblib.dump(reg_rf, 'flight_fare_model.pkl')
    joblib.dump(feature_columns, 'model_columns.pkl')
    print("Model trained and saved successfully!")

    print("Model trained and saved successfully!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Train Flight Fare Prediction Model')
    parser.add_argument('--test-run', action='store_true', help='Run in test mode (fewer samples)')
    parser.add_argument('--data-path', type=str, help='Path to real CSV dataset')
    
    args = parser.parse_args()
    
    if args.data_path:
        print(f"Loading data from {args.data_path}...")
        try:
            # Here we would add specific logic to load real data
            # For this demo, we'll just print a message and exit or fallback
            print("Real data loading logic would go here. Falling back to synthetic for now.")
            train_model()
        except Exception as e:
            print(f"Error loading data: {e}")
            sys.exit(1)
    elif args.test_run:
        print("Running in TEST MODE (Data generation only, no save)...")
        _ = generate_synthetic_data(num_samples=100)
        print("Test run complete.")
    else:
        train_model()
