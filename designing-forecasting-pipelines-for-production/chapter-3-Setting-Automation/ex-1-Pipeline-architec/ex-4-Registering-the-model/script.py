import mlflow
import datetime
from mlforecast import MLForecast

experiment_name = "ml_forecast"
try:
    mlflow.create_experiment(name=experiment_name)
    meta = mlflow.get_experiment_by_name(experiment_name)
    print(f"Setting a new experiment {experiment_name}")
except:
    print(f"Experiment {experiment_name} exists, pulling the metadata")
    meta = mlflow.get_experiment_by_name(experiment_name)

# Setup the run name and time
run_time = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
run_name = f"lightGBM6_{run_time}"

# Start the run
with mlflow.start_run(experiment_id=meta.experiment_id, run_name=run_name) as run:
    # Log the model
    # mlforecast.flavor.log_model(model=mlf, artifact_path="prod_model")
    print(f"MLflow Run created - Name: {run_name}, ID: {run.info.run_id}")
