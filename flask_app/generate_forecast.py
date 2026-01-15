
import pandas as pd
from lightgbm import LGBMRegressor
from xgboost import XGBRegressor
from sklearn.linear_model import LinearRegression
from mlforecast import MLForecast
try:
    from mlforecast.prediction_intervals import PredictionIntervals
except ImportError:
    PredictionIntervals = None
from utilsforecast.plotting import plot_series
import plotly.io as pio

def generate_forecast():
    """
    Generates a forecast plot and saves it as an HTML file.
    """
    print("Loading data...")
    # Load the training data
    df = pd.read_csv("train_trimmed.csv")
    df['ds'] = pd.to_datetime(df['ds'])
    df = df.sort_values(by=['unique_id', 'ds'])
    print("Data loaded.")

    print("Setting up MLForecast...")
    # Set up the MLForecast object with models and frequency
    ml_models = [LGBMRegressor(), XGBRegressor(), LinearRegression()]
    mlf = MLForecast(
        models=ml_models,
        freq='H',
        lags=list(range(1, 24)),
        date_features=['year', 'month', 'day', 'dayofweek', 'quarter', 'week', 'hour']
    )
    print("MLForecast setup complete.")

    print("Fitting model...")
    # Fit the model to the training data
    if PredictionIntervals:
        mlf.fit(data=df,
                prediction_intervals=PredictionIntervals(n_windows=5, window_size=72, method="conformal_distribution"))
    else:
        mlf.fit(data=df)
    print("Model fitting complete.")

    print("Generating forecast...")
    # Generate forecasts for the next 72 hours with 95% confidence
    if PredictionIntervals:
        ml_forecast = mlf.predict(72, level=[95])
    else:
        ml_forecast = mlf.predict(72)
    print("Forecast generation complete.")

    print("Loading test data...")
    # Load the test data
    test = pd.read_csv("test_trimmed.csv")
    test['ds'] = pd.to_datetime(test['ds'])
    test = test.sort_values(by=['unique_id', 'ds'])
    print("Test data loaded.")

    print("Generating plot...")
    # Plot the forecast results
    if PredictionIntervals:
        fig = plot_series(test, ml_forecast, level=[95], engine="plotly").update_layout(height=400)
    else:
        fig = plot_series(test, ml_forecast, engine="plotly").update_layout(height=400)
    print("Plot generation complete.")

    print("Saving plot to HTML...")
    # Save the plot to an HTML file
    plot_div = pio.to_html(fig, full_html=False, include_plotlyjs='cdn')
    with open("templates/plot_div.html", "w") as f:
        f.write(plot_div)
    print("Plot saved to templates/plot_div.html.")

if __name__ == '__main__':
    generate_forecast()
