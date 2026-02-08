# Flight Fare Calculator Web App ✈️

A complete, free-to-use web application that predicts flight ticket prices using machine learning. Built with Flask, Scikit-learn, and Bootstrap.

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Flask](https://img.shields.io/badge/Flask-2.0%2B-green)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-purple)
![CI Status](https://github.com/Aaryankansari/flight-fare-calculator-app/actions/workflows/python-app.yml/badge.svg)

## 🚀 Features

- **Accurate Predictions**: Uses a Random Forest Regressor trained on synthetic flight data.
- **User-Friendly Interface**: Clean and responsive design using Bootstrap 5.
- **Self-Contained**: No external paid APIs required.
- **End-to-End**: Data generation -> Model training -> Backend -> Frontend.
- **CI/CD Integrated**: Automated testing on every push.

## 🛠️ Tech Stack

- **Backend**: Python, Flask
- **Machine Learning**: Scikit-Learn, Pandas, NumPy, Joblib
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Deployment**: Docker, Procfile (Heroku/Render ready)

## 📂 Project Structure

```
flight-fare-prediction/
├── app.py                  # Flask backend application
├── train_model.py          # Data generation and model training script
├── flight_fare_model.pkl   # Trained machine learning model
├── model_columns.pkl       # Serialized model columns
├── requirements.txt        # Project dependencies
├── Procfile                # Deployment configuration
├── Dockerfile              # Docker configuration
├── README.md               # Project documentation
├── data/                   # Directory for real datasets
└── templates/
    ├── index.html          # Input form template
    └── result.html         # Prediction result template
```

## 🏁 Getting Started

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Aaryankansari/flight-fare-calculator-app.git
   cd flight-fare-calculator-app
   ```

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

## ☁️ Deployment

### Deploy to Render (Free Tier)

1. Create a new **Web Service** on [Render](https://render.com/).
2. Connect your GitHub repository.
3. Render will automatically detect the `Procfile` and `requirements.txt`.
4. Click **Deploy**.

### Deploy to Heroku

1. Create a new app on Heroku.
2. Connect your GitHub repository.
3. Deploy branch `main`.

## 📊 Using Real Data

To train the model on a real dataset (e.g., from Kaggle):

1. Download a dataset like [Flight Price Prediction](https://www.kaggle.com/datasets/nikhilmittal/flight-fare-prediction-mh).
2. Save the CSV file to `data/your_dataset.csv`.
3. Run the training script with the data path:
   ```bash
   python train_model.py --data-path data/your_dataset.csv
   ```
   *(Note: You may need to adjust `train_model.py` slightly depending on the column names of your specific dataset.)*

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open-source and free to use.
