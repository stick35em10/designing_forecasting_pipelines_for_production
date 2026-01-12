from lightgbm import LGBMRegressor
from xgboost import XGBRegressor
from sklearn.linear_model import LinearRegression
from mlforecast import MLForecast
from mlforecast.forecast import PredictionIntervals

import pandas as pd

ml_models = [LGBMRegressor(), XGBRegressor(), LinearRegression()]

mlf = MLForecast(
    models= ml_models,  
    freq='h', 
    lags=list(range(1, 24)), 
    date_features=['year', 'month', 'day', 'dayofweek', 'quarter', 'week', 'hour'])

# Fit the model to the training data
#import pandas as pd 

train = pd.read_csv("train_trimmed.csv")
train['ds'] = pd.to_datetime(train['ds'])
mlf.fit(df=train,  fitted=True, 
prediction_intervals=PredictionIntervals(n_windows=5, h=72, method="conformal_distribution"))

# Generate forecasts for the next 72 hours with 95% confidence
ml_forecast = mlf.predict(72, level=[95])

print(ml_forecast.head())