import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import seaborn as sns

# Function to generate synthetic data
def generate_data(num_samples=1000, start_date='2023-01-01'):
    np.random.seed(42)
    dates = pd.to_datetime(pd.date_range(start=start_date, periods=num_samples, freq='D'))
    
    # Feature 1: Time-based trend
    time_feature = np.arange(num_samples) / 365.0
    
    # Feature 2: Seasonal component
    seasonal_feature = 10 * np.sin(np.arange(num_samples) * 2 * np.pi / 90) # Quarterly seasonality
    
    # Feature 3: Random noise
    noise = np.random.normal(loc=0, scale=2, size=num_samples)
    
    # Target variable: a combination of features with some interaction
    target = 50 + 2 * time_feature + 0.5 * seasonal_feature + noise + \
             0.1 * (time_feature * seasonal_feature) # Interaction term

    data = pd.DataFrame({
        'date': dates,
        'time_feature': time_feature,
        'seasonal_feature': seasonal_feature,
        'target': target
    })
    data = data.set_index('date')
    return data

# Function to train a model and make predictions
def train_and_predict(data):
    X = data[['time_feature', 'seasonal_feature']]
    y = data['target']
    
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X, y)
    
    predictions = model.predict(X)
    data['predictions'] = predictions
    return data, model

# Main script for model drift detection simulation
if __name__ == "__main__":
    print("Generating synthetic data...")
    data = generate_data(num_samples=500)
    
    print("Training initial model and making predictions...")
    data, model = train_and_predict(data)
    
    # Simulate a period where the model is in production
    production_data = data.copy()

    # --- Model Drift Detection ---
    print("\nSimulating model drift detection...")

    # For simplicity, let's assume 'model drift' is detected if the mean absolute error
    # on new data exceeds a certain threshold, or if statistical properties change.
    
    # Example 1: Monitoring prediction error on new data (requires true labels)
    # This usually means you have a delay in receiving true labels, or you use a proxy.
    
    # Let's simulate new incoming data where the relationship slightly changes
    print("Generating new data with slight drift...")
    drift_data = generate_data(num_samples=100, start_date='2024-06-01')
    
    # Apply a drift: e.g., the target variable relationship with time_feature changes
    drift_data['target'] = drift_data['target'] * 1.1 + 5 # Increase target values
    
    # Make predictions on the drift data using the *original* trained model
    drift_X = drift_data[['time_feature', 'seasonal_feature']]
    drift_predictions = model.predict(drift_X)
    drift_data['predictions'] = drift_predictions

    # Calculate error on the drift data
    drift_mae = np.mean(np.abs(drift_data['target'] - drift_data['predictions']))
    print(f"Mean Absolute Error on drift data: {drift_mae:.2f}")

    # Define a threshold for drift detection (e.g., 20% higher than training MAE)
    # For this example, let's use a arbitrary threshold
    drift_threshold = 10.0 # This should ideally be learned or set based on domain knowledge

    if drift_mae > drift_threshold:
        print(f"!!! ALERT: Model drift detected! MAE ({drift_mae:.2f}) exceeded threshold ({drift_threshold:.2f}).")
    else:
        print(f"No significant model drift detected. MAE ({drift_mae:.2f}) is within threshold ({drift_threshold:.2f}).")

    # Example 2: Monitoring input feature distribution changes (no true labels needed)
    # This is often done using statistical tests like KS-test or population stability index (PSI)

    # Compare distribution of 'time_feature' in production data vs. drift data
    print("\nComparing input feature distributions...")
    
    plt.figure(figsize=(12, 6))
    sns.histplot(production_data['time_feature'], color='blue', label='Production Data', kde=True, stat='density', alpha=0.5)
    sns.histplot(drift_data['time_feature'], color='red', label='Drift Data', kde=True, stat='density', alpha=0.5)
    plt.title('Distribution of Time Feature: Production vs. Drift Data')
    plt.xlabel('Time Feature')
    plt.ylabel('Density')
    plt.legend()
    plt.savefig('time_feature_distribution_drift.png')
    print("Saved 'time_feature_distribution_drift.png' showing feature distribution comparison.")

    # More advanced drift detection would involve statistical tests here
    # For a simple example, we can just visually inspect or check mean/std deviation changes
    
    prod_mean_time = production_data['time_feature'].mean()
    drift_mean_time = drift_data['time_feature'].mean()
    
    print(f"Production 'time_feature' mean: {prod_mean_time:.2f}")
    print(f"Drift 'time_feature' mean: {drift_mean_time:.2f}")

    if np.abs(prod_mean_time - drift_mean_time) > 0.5: # Arbitrary threshold
        print("!!! ALERT: Significant change in 'time_feature' distribution detected!")
    else:
        print("No significant change in 'time_feature' distribution.")

    print("\nModel drift simulation complete.")
    