# Import LGBMRegressor from lightgbm
from lightgbm import LGBMRegressor

# Instantiate the model
#Instantiate a LGBMRegressor model with 100 estimators and a learning rate of 0.05.
#model = LGBMRegressor(n_estimators=____, learning_rate=____)
model = LGBMRegressor(n_estimators=100, learning_rate=0.05)

# Set the model parameters
# Create a dictionary named params that 
# includes the frequency ("h"), 
# lags (1-24), and date features 
# ("month", "day", "dayofweek", "week", and "hour").
params = {
  "freq": "h",
  "lags": list(range(1, 24)),
  "date_features": ["month", "day", "dayofweek", "week", "hour"]
}