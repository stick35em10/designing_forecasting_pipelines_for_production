from lightgbm import LGBMRegressor
from xgboost import XGBRegressor
from sklearn.linear_model import LinearRegression
from mlforecast import MLForecast
from mlforecast.forecast import PredictionIntervals
from utilsforecast.losses import mape, rmse # Corrected import path

import pandas as pd

# Load the training data (from script 9)
df = pd.read_csv("ex-8-Working-with-a-forecast-object/ex-9-Forecasting-with-ML-Models/train_trimmed.csv")
df['ds'] = pd.to_datetime(df['ds'])
df = df.sort_values(by=['unique_id', 'ds'])

# Set up the MLForecast object with models and frequency (from script 9)
ml_models = [LGBMRegressor(), XGBRegressor(), LinearRegression()]

mlf = MLForecast(
    models=ml_models,
    freq='h',
    lags=list(range(1, 24)),
    date_features=['year', 'month', 'day', 'dayofweek', 'quarter', 'week', 'hour']
)

# Fit the model to the training data (from script 9)
mlf.fit(data=df,
prediction_intervals=PredictionIntervals(n_windows=5, window_size=72, method="conformal_distribution"))

# Generate forecasts for the next 72 hours with 95% confidence (from script 9)
ml_forecast = mlf.predict(72, level=[95])

# Load the test data (new addition for script 10)
test = pd.read_csv("ex-8-Working-with-a-forecast-object/ex-9-Forecasting-with-ML-Models/test_trimmed.csv")
test['ds'] = pd.to_datetime(test['ds'])
test = test.sort_values(by=['unique_id', 'ds'])

# Combine the data (original script 10)
fc = ml_forecast.merge(test, how="left", on="ds")

fc_performance = None

for model in ["LGBMRegressor", "XGBRegressor", "LinearRegression"]:
    # Prepare DataFrame for loss functions
    temp_fc_for_losses = fc[['unique_id_x', 'y', model]].copy() # Changed 'unique_id' to 'unique_id_x'

    m = mape(df=temp_fc_for_losses, models=[model], id_col="unique_id_x", target_col="y")[model].iloc[0] # Changed 'unique_id' to 'unique_id_x'
    r = rmse(df=temp_fc_for_losses, models=[model], id_col="unique_id_x", target_col="y")[model].iloc[0] # Changed 'unique_id' to 'unique_id_x'

    perf = {"model": model, "mape": m, "rmse": r} # Removed coverage
    if fc_performance is None:
        fc_performance = pd.DataFrame([perf])
    else:
        fc_performance = pd.concat([fc_performance, pd.DataFrame([perf])])

# Sort the performance metrics by rmse
print(fc_performance.sort_values("rmse"))