from flask import Flask, render_template
from lightgbm import LGBMRegressor
from xgboost import XGBRegressor
from sklearn.linear_model import LinearRegression
from mlforecast import MLForecast
from mlforecast.forecast import PredictionIntervals
from utilsforecast.plotting import plot_series
import pandas as pd
import plotly

app = Flask(__name__)

@app.route('/')
def plot():
    # Load the training data
    df = pd.read_csv("train_trimmed.csv")
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
    mlf.fit(df,
            prediction_intervals=PredictionIntervals(n_windows=5, h=72, method="conformal_distribution"))

    # Generate forecasts for the next 72 hours with 95% confidence
    ml_forecast = mlf.predict(72, level=[95])

    # Load the test data
    test = pd.read_csv("test_trimmed.csv")
    test['ds'] = pd.to_datetime(test['ds'])
    test = test.sort_values(by=['unique_id', 'ds'])

    # Plot the forecast results
    fig = plot_series(test, ml_forecast, level=[95], engine="plotly").update_layout(height=400)
    
    # Convert the plot to HTML
    plot_html = fig.to_html(full_html=False)

    return render_template('index.html', plot_html=plot_html)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
