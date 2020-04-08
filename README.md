# covid19
This is an experimental API to relay covid-19 (Coronovirus) cases' data in a useful and consumable way.

This project is written in Python. It supplies data about Covid-19 stats per country.

## Data sources
The European CDC publishes daily statistics on the COVID-19 pandemic. Not just for Europe, but for the entire world.

The ECDC makes all their data available in a daily updated clean downloadable file. This gets updated daily reflecting data collected up to 6:00 and 10:00 CET. The data made public via the downloadable data file is published at 1pm CET, and is used to produce a page that gets updated daily under the name Situation Update Worldwide.
https://www.ecdc.europa.eu/en/geographical-distribution-2019-ncov-cases

## install
To run this project locally

I'll recommend using virtualenv.

pip3.7 install virtualenv

virtualenv venv --python=python3.7

-- this is important to ensure you are running things in the right envrinoment
source venv/bin/activate

pip install Flask-Restful
pip install prometheus_client
pip install requests

## Run
Python app.py
navigate to localhost:5000/<country-name>
e.g. localhost:5000/ireland