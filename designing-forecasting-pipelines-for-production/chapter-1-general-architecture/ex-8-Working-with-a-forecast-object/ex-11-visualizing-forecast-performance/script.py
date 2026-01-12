from lightgbm import LGBMRegressor
from xgboost import XGBRegressor
from sklearn.linear_model import LinearRegression
from mlforecast import MLForecast
from mlforecast.forecast import PredictionIntervals
from utilsforecast.plotting import plot_series # Added plot_series import

import pandas as pd

# Load the training data
df = pd.read_csv("ex-8-Working-with-a-forecast-object/ex-9-Forecasting-with-ML-Models/train_trimmed.csv")
df['ds'] = pd.to_datetime(df['ds'])
df = df.sort_values(by=['unique_id', 'ds'])

# Set up the MLForecast object with models and frequency
ml_models = [LGBMRegressor(), XGBRegressor(), LinearRegression()]

mlf = MLForecast(
    models=ml_models,
    freq='h',
    lags=list(range(1, 24)),
    date_features=['year', 'month', 'day', 'dayofweek', 'quarter', 'week', 'hour']
)

# Fit the model to the training data
mlf.fit(data=df,
prediction_intervals=PredictionIntervals(n_windows=5, window_size=72, method="conformal_distribution"))

# Generate forecasts for the next 72 hours with 95% confidence
ml_forecast = mlf.predict(72, level=[95])

# Load the test data
test = pd.read_csv("ex-8-Working-with-a-forecast-object/ex-9-Forecasting-with-ML-Models/test_trimmed.csv")
test['ds'] = pd.to_datetime(test['ds'])
test = test.sort_values(by=['unique_id', 'ds'])

# Plot the forecast results
fig = plot_series(test, ml_forecast, level=[95], engine="plotly").update_layout(height=400)
fig.show()