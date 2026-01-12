#https://campus.datacamp.com/courses/designing-forecasting-pipelines-for-production/general-architecture?ex=6
import pandas as pd

df = pd.read_csv("ex-6-Preparing-and-visualizing-the-data/data/data.csv")
ts = df[["period","y"]]
# Convert the period column to datetime and sort the data by period
#ts["____"] = pd.____(ts["period"])
#ts = ts.____("period")

# Convert the period column to datetime and sort the data by period
ts.dtypes
ts["period"] = pd.to_datetime(ts["period"])
ts.dtypes

ts = ts.sort_values("period")
ts.head()

# Rename the columns and add a unique_id column
ts = ts.rename(columns = {"period": "ds", "value": "y"})
ts["unique_id"] = 1

print(ts.head())

from statsforecast import StatsForecast

fig = StatsForecast.plot(ts, engine="plotly")
fig.show()