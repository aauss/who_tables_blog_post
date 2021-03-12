# Repo for the Medium blog post on the data quality of WHO's COVID-19 data
Contains code to acquire and analyze data from https://covid19.who.int/table

## Install
If you want to run the code yourself and you have conda, just run `conda env create -f env.yml` and you are good to go.

## Content
This repo contains three things: a scraper (as .py, and .ipynb), scraped files from WHO placed in to the `scraped` folder, and a notebook (analysis.ipynb) in which I analyze WHO's data for reporting behavior, regional differences in the COVID-19 spread, and the relevance of epidemiological information provided in the scraped data.