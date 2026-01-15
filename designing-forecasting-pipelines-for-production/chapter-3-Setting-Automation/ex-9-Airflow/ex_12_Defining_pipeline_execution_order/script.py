#Set the API check pipeline and check status tasks.
#Set the data validation pipeline tasks.
#Set the forecast pipeline tasks.


# Set the API check pipeline tasks
check_api >> check_status >> [data_refresh, no_updates]

data_refresh >> [data_validation, data_failure]

# Set the data validation pipeline tasks
data_validation >> check_validation >> [data_valid, data_invalid]

# Set the forecast pipeline tasks
data_valid >> forecast_refresh >> forecast_pipeline

print(f"DAG '{dag.dag_id}' ready with {len(dag.tasks)} tasks")
