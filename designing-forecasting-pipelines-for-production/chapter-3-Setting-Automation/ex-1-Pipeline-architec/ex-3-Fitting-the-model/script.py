from lightgbm import LGBMRegressor
from mlforecast import MLForecast
import pandas as pd

# Instantiate the model
model = LGBMRegressor(n_estimators=100, learning_rate=0.05)

# Set the model parameters
params = {
  "freq": "h",
  "lags": list(range(1, 24)),
  "date_features": ["month", "day", "dayofweek", "week", "hour"]
}

# Create a dummy ts DataFrame for demonstration purposes
data = {
    'unique_id': ['A'] * 48 + ['B'] * 48,
    'ds': pd.to_datetime(pd.date_range(start='2023-01-01', periods=48, freq='h').tolist() * 2),
    'y': [i + 10 for i in range(48)] + [i + 20 for i in range(48)]
}
ts = pd.DataFrame(data)

# Create an MLForecast instance
mlf = MLForecast(
    models=model,
    freq=params["freq"],
    lags=params["lags"],
    date_features=params["date_features"]
)

# Fit mlf to the time series data
mlf.fit(ts)

print("MLForecast model fitted successfully!")