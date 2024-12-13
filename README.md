# JobTrendInsights 


JobTrendInsights is a web scraping and data analysis project that focuses on extracting job listings from Indeed and Welcome to the Jungle, analyzing trends in job searches, and presenting the results through a Flask web application.

## Project Overview

This project aims to:
1. Scrape job data from Indeed and Welcome to the Jungle
2. Store the collected data efficiently
3. Perform data analysis to identify trends in job searches
4. Present the findings through a user-friendly web interface

## Features

- Web scraping modules for Indeed and Welcome to the Jungle
- Welcome to the Jungle workflow : 
    - Job number element 
    - nom de l'annonce 
    - l'entreprise de l'annonce 
    - type du job: cdi, cdd, stage 
    - adresse de l'annonce
    - date de l'annonce
    - Description de l'annonce
- Data storage solution for scraped job listings
- Data analysis tools to identify trends in the job market
- Flask web application to search and display job offers based on job title and date

## Project Structure
JobTrendInsights/
│
├── src/
│ └── job_market_analyzer/
│ ├── scrapers/
│ ├── data_storage/
│ ├── analysis/
│ ├── utils/
│ ├── config/
│ └── webapp/
│
├── config/
├── research/
├── templates 
├── static/
│ ├── css/
│ └── js/
│
├── .github/
│ └── workflows/
│
├── requirements.txt
├── setup.py
└── run.py


## Installation

1. Clone the repository:

``
git clone https://github.com/boudia-abderaouf/job-market-analyzer.git
cd job-market-analyzer
``

2. Create a virtual environment and activate it:

``python -m venv venv
source venv/bin/activate # On Windows, use venv\Scripts\activate
``

3. Install the required packages:
``
pip install -r requirements.txt
``


## Usage

1. Configure the scraping settings in `config/config.yaml`
2. Run the scraping and analysis pipeline:
``
python src/job_market_analyzer/main.py
``

3. Start the Flask web application:
``
python run.py
``

4. Open your web browser and navigate to `http://localhost:5000`

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

