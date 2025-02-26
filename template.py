import os 
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)

project_name = 'ml_finals'

list_of_file = [
    f"src/{project_name}/models/notebook/linear-regression.ipynb",
    f"src/{project_name}/models/notebook/logistic-regression.ipynb",
    f"src/{project_name}/models/notebook/SVM.ipynb",
    f"src/{project_name}/models/notebook/random-forest.ipynb",
    f"src/{project_name}/models/notebook/Naive-bayes.ipynb",
    f"src/{project_name}/models/notebook/Decision-tree.ipynb",
    f"src/{project_name}/models/notebook/K-means-clustering.ipynb",
    f"src/{project_name}/models/notebook/KNN.ipynb",
    f"src/{project_name}/models/notebook/ADAboost.ipynb",
    f"src/{project_name}/models/notebook/XGboost.ipynb",
    f"src/{project_name}/models/data/data.csv",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/exceeption.py",
    f"src/{project_name}/models/notebook/XGboost.ipynb",
    f"src/{project_name}/components/__init__.py",
    "app.py",
    'setup.py',
    'requirements.txt',
    'Dockerfile'
]


for filepath in list_of_file:
    filepath = Path(filepath)
    filedir, filename = filepath.parent, filepath.name  # Correct way to get directory & file name

    if filedir != "":
        filedir.mkdir(parents=True, exist_ok=True)  # Create directory properly
        logging.info(f"Creating directory {filedir} for the file: {filename}")

    if not filepath.exists() or filepath.stat().st_size == 0:
        filepath.touch()  # Create an empty file
        logging.info(f"Creating the file: {filename}")
    else:
        logging.info(f"File {filename} already exists")


