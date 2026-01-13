import pandas as pd
import numpy as np

# Dummy data for fc_log_test (first 14 forecasts)
data_test = {'forecast_start': pd.to_datetime(pd.date_range(start='2023-01-01', periods=14, freq='D')),
             'rmse': np.random.uniform(10, 30, 14)}
fc_log_test = pd.DataFrame(data_test)

# Dummy data for fc_log (remaining forecasts)
data_log = {'forecast_start': pd.to_datetime(pd.date_range(start='2023-01-15', periods=30, freq='D')),
            'rmse': np.random.uniform(10, 40, 30)}
fc_log = pd.DataFrame(data_log)

#Define the threshold level from 
#    fc_log_test by adding three standard deviations to 
#    the RMSE mean, storing as rmse_threshold.

#Calculate the RMSE moving average using 7-day and 
#    14-day rolling windows for fc_log.

# Set threshold: mean + 3 standard deviations
rmse_threshold = fc_log_test["rmse"].mean() + 3 * fc_log_test["rmse"].std()

# Create rolling window averages for RMSE
fc_log["rmse_ma_7"] = fc_log["rmse"].rolling(window=7).mean()
fc_log["rmse_ma_14"] = fc_log["rmse"].rolling(window=14).mean()

print(f"RMSE threshold: {round(rmse_threshold, 2)}")
print()
print("Forecast log with rolling averages:")
print(fc_log[["forecast_start", "rmse", "rmse_ma_7", "rmse_ma_14"]].head(20))
