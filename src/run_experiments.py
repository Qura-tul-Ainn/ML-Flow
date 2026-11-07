
"""Run 10 training iterations with different settings, all logged to MLflow."""

from src.config import load_params
from src.train import train_and_log

# TODO S1.8: 10 different experiment settings
EXPERIMENTS = [
    {"model": "random_forest", "n_estimators": 50, "max_depth": 4},
    {"model": "random_forest", "n_estimators": 100, "max_depth": 6},
    {"model": "random_forest", "n_estimators": 200, "max_depth": 8},
    {"model": "random_forest", "n_estimators": 100, "max_depth": 10},
    {"model": "random_forest", "n_estimators": 300, "max_depth": 10},
    {"model": "random_forest", "n_estimators": 100, "max_depth": 12},
    {"model": "random_forest", "n_estimators": 50, "min_samples_leaf": 10},
    {"model": "logistic_regression", "C": 0.1},
    {"model": "logistic_regression", "C": 1.0},
    {"model": "logistic_regression", "C": 10.0},
]


def main():
    base = load_params()["train"]

    print(f"Running {len(EXPERIMENTS)} experiments...")

    for i, changes in enumerate(EXPERIMENTS, start=1):

        # TODO S1.9: Merge base settings with experiment changes
        config = {**base, **changes}

        # Train and log each experiment
        train_and_log(config, run_name=f"exp-{i:02d}")

    print("Done. Run `mlflow ui` and compare the runs.")


if __name__ == "__main__":
    main()
