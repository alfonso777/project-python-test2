import mlflow
from mlflow import log_metric, log_param, log_artifact

mlflow.set_experiment("My_Experiment")
with mlflow.start_run(run_name="run_abc") as run:
    # Log a parameter (key-value pair)
    log_param("param1", 6)
    log_param("param2", 10)
    # Log a metric; metrics can be updated throughout the run
    log_metric("foo1", 11)
    log_metric("foo", 21)
    log_metric("foo3", 33)
    # Log an artifact (output file)
    with open("output.txt", "w") as f:
        f.write("Hello world mate!")
        log_artifact("output.txt")
