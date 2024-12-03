import os 
from pathlib import Path 
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]:%(message)s')

project_name = 'job_market_analyzer'

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/scrapers/__init__.py",
    f"src/{project_name}/scrapers/indeed_scraper.py",
    f"src/{project_name}/scrapers/wttj_scraper.py",
    f"src/{project_name}/data_storage/__init__.py",
    f"src/{project_name}/data_storage/database.py",
    f"src/{project_name}/analysis/__init__.py",
    f"src/{project_name}/analysis/trend_analyzer.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/helpers.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/webapp/__init__.py",
    f"src/{project_name}/webapp/routes.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "requirements.txt",
    "setup.py",
    "research/indeed_scraper.ipynb",
    "research/wttj_scraper.ipynb",
    "research/data_exploration.ipynb",
    "templates/index.html",
    "templates/results.html",
    "static/css/style.css",
    "static/js/main.js",
    "run.py"
]




for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)


    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            logging.info(f"Creating empty file: {filepath}")


    else:
        logging.info(f"{filename} is already exists")