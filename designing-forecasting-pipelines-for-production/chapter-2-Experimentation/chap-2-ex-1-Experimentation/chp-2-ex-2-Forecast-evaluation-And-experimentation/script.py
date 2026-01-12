import numpy as np
import pandas as pd

def mape(y_true, y_pred):
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100

def rmse(y_true, y_pred):
    return np.sqrt(np.mean((y_true - y_pred)**2))

def coverage(y_true, y_lower, y_upper):
    return np.mean((y_true >= y_lower) & (y_true <= y_upper)) * 100

# Placeholder for fc DataFrame
data = {
    "y": [100, 110, 105, 115, 120],
    "LGBMRegressor": [102, 108, 107, 113, 122],
    "LGBMRegressor-lo-95": [95, 100, 98, 105, 115],
    "LGBMRegressor-hi-95": [108, 116, 114, 120, 128],
    "XGBRegressor": [98, 112, 103, 117, 118],
    "XGBRegressor-lo-95": [90, 105, 96, 110, 111],
    "XGBRegressor-hi-95": [106, 119, 110, 124, 125],
    "LinearRegression": [105, 105, 110, 110, 115],
    "LinearRegression-lo-95": [98, 98, 103, 103, 108],
    "LinearRegression-hi-95": [112, 112, 117, 117, 122],
}
fc = pd.DataFrame(data)

performance_metrics = []

# Loop through models and calculate metrics
for model in ["LGBMRegressor", "XGBRegressor", "LinearRegression"]:
    performance_metrics.append({
        "model": model,
        "mape": mape(fc["y"], fc[model]),
        "rmse": rmse(fc["y"], fc[model]),
        "coverage": coverage(fc["y"], fc[f"{model}-lo-95"], fc[f"{model}-hi-95"])
    })

# Create DataFrame and sort by RMSE
fc_performance = pd.DataFrame(performance_metrics).sort_values("rmse")

print(fc_performance)