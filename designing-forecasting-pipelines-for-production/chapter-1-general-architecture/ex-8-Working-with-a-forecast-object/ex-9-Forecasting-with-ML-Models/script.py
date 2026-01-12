from lightgbm import LGBMRegressor
from xgboost import XGBRegressor
from sklearn.linear_model import LinearRegression
from mlforecast import MLForecast
from mlforecast.forecast import PredictionIntervals

import pandas as pd

# Define the ML models
ml_models = [LGBMRegressor(), XGBRegressor(), LinearRegression()]

# Load the training data
df = pd.read_csv("ex-8-Working-with-a-forecast-object/ex-9-Forecasting-with-ML-Models/train_trimmed.csv")
df['ds'] = pd.to_datetime(df['ds'])
df = df.sort_values(by=['unique_id', 'ds'])

# Set up the MLForecast object with models and frequency

mlf = MLForecast(
    models= ml_models,  
    freq='h', 
    lags=list(range(1, 24)), 
    date_features=['year', 'month', 'day', 'dayofweek', 'quarter', 'week', 'hour'])

# Fit the model to the training data
mlf.fit(df=df,  fitted=True, 
prediction_intervals=PredictionIntervals(n_windows=5, h=72, method="conformal_distribution"))

# Generate forecasts for the next 72 hours with 95% confidence
ml_forecast = mlf.predict(72, level=[95])

print(ml_forecast.head())