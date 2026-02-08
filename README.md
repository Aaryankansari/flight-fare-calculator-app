# Flight Fare Calculator Web App ✈️

A complete, free-to-use web application that predicts flight ticket prices using machine learning. Built with Flask, Scikit-learn, and Bootstrap.

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Flask](https://img.shields.io/badge/Flask-2.0%2B-green)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-purple)

## 🚀 Features

- **Accurate Predictions**: Uses a Random Forest Regressor trained on synthetic flight data.
- **User-Friendly Interface**: Clean and responsive design using Bootstrap 5.
- **Self-Contained**: No external paid APIs required.
- **End-to-End**: Data generation -> Model training -> Backend -> Frontend.

## 🛠️ Tech Stack

- **Backend**: Python, Flask
- **Machine Learning**: Scikit-Learn, Pandas, NumPy, Joblib
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Deployment**: Docker (optional)

## 📂 Project Structure

```
flight-fare-prediction/
├── app.py                  # Flask backend application
├── train_model.py          # Data generation and model training script
├── flight_fare_model.pkl   # Trained machine learning model
├── model_columns.pkl       # Serialized model columns
├── requirements.txt        # Project dependencies
├── Dockerfile              # Docker configuration
├── README.md               # Project documentation
└── templates/
    ├── index.html          # Input form template
    └── result.html         # Prediction result template
```

## 🏁 Getting Started

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository** (if applicable) or navigate to the project directory.

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Train the mode** (Optional: A pre-trained model is generated if you run this):
   ```bash
   python train_model.py
   ```
   This will generate `flight_fare_model.pkl` and `model_columns.pkl`.

### Running the App

1. **Start the Flask server**:
   ```bash
   python app.py
   ```

2. **Open your browser** and go to:
   [http://127.0.0.1:5000](http://127.0.0.1:5000)

## 🐳 Docker Support

To run the application using Docker:

1. **Build the image**:
   ```bash
   docker build -t flight-fare-app .
   ```

2. **Run the container**:
   ```bash
   docker run -p 5000:5000 flight-fare-app
   ```

## 📸 Usage

1. Select your **Departure Date & Time**.
2. Select your **Arrival Date & Time**.
3. Choose **Source** and **Destination** cities.
4. Select the number of **Stops**.
5. Pick your preferred **Airline**.
6. Click **Predict Price** to see usage estimate.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open-source and free to use.
