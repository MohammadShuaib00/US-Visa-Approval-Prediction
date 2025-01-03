import os
from pathlib import Path
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="[%(asctime)s]: %(message)s")

# Input for project name
while True:
    project_name = input("Enter the source project name: ")
    if project_name != '':
        break

# List of files and directories to create
list_of_files = [
    ".github/workflows/.gitkeep",
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion",
    f"{project_name}/components/data_transformation",
    f"{project_name}/components/data_validation",
    f"{project_name}/components/model_trainer",
    f"{project_name}/components/model_pusher",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/entity_config.py",
    f"{project_name}/entity/artifact_config.py",
    f"{project_name}/constant/__init__.py",
    f"{project_name}/constant/training.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/training_pipeline.py",
    f"{project_name}/pipeline/prediction_pipeline.py",
    f"{project_name}/data",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/model/__init__.py",
    f"{project_name}/utils/model/estimator.py",
    f"{project_name}/utils/metric/__init__.py",
    f"{project_name}/utils/metric/get_classification_metric.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/logger/logging.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/exception/exception.py",
    "notebook/experiment.ipynb",
    "templates/index.html",
    "static/style.css",
    "requirements.txt",
    "setup.py",
    "app.py",
    "test.py",
    "push_data_into_database.py",
    "Dockerfile"
]

# Creating the directories and files
for file in list_of_files:
    filepath = Path(file)
    filedir, filename = os.path.split(filepath)

    # Create directory if it doesn't exist
    if filedir != "":
        try:
            os.makedirs(filedir, exist_ok=True)
            logging.info(f"Directory created: {filedir}")
        except Exception as e:
            logging.error(f"Failed to create directory {filedir}: {e}")

    # Create the file if it doesn't exist or is empty
    if not filepath.exists() or filepath.stat().st_size == 0:
        try:
            with open(filepath, "w"):
                pass  # Just create an empty file
            logging.info(f"File created: {filepath}")
        except Exception as e:
            logging.error(f"Failed to create file {filepath}: {e}")
    else:
        logging.info(f"File already exists: {filepath}")
