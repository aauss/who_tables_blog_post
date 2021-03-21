# Repo for the Medium blog post on the data quality of WHO's COVID-19 data

## Install

If you want to run the code yourself and you have conda, just run `conda env create -f env.yml` and you are good to go.

### Packages

For the analyses, I used matplotlib, seaborn, and altair for plotting. For data processing, I used pandas, for data scraping requests, and for data modelling scikit-learn. I must not forget, that all my analyses are shown as .ipynb for which I used JupyterLab.

## Motivation

WHO was on the main stage during the uprise of the COVID-19 pandemic in 2020. One year later, I wanted to see how far WHO got as the main institution for public health. How good is their data and what can it answer? Furthermore, I always was intersted in other regions and their situation which is rarely covered in German mainstream news. Thus, I scraped and analyzed WHO's publically available data on COVID-19.

## Files

This repo contains three things: a scraper (as .py, and .ipynb), scraped files from [WHO](https://covid19.who.int/table) as CSVs placed in to the `scraped` folder, and a notebook (analysis.ipynb) in which I analyze WHO's data for reporting behavior, regional differences in the COVID-19 spread, and the relevance of epidemiological information provided by WHO form the perspective of a machine learning model.

## Results

My analyses can be summarized into the following points:

1. **Data is changed retrospectivally**. E.g., almost 17% of all reported 7-day-incidence (amount of cases in 7 days per 100.000 residents) in the scraped data changed when comparing them to a self-calculated 7-day-incidence using more recent data.

2. **Reporting behavior is dependent on region.**
    - Reporting behavior is vastly different between regions. A majority (~90%) of the European and the Middle Eastern countries report new cases after less than 7 days. 90% of the American and African countries, on the other hand, report new cases after more than 7 days. 
    - While this difference in reporting could be due to differently severe infection dynamics, Europe and Americas have the highest, relative amount of cases: A frequent and less-frequent reporting region.
3. I compared two models to predict future case numbers.One was using past case numbers and geographical information. The other model used the same input but additionally included WHO transmission classification (information on how currently cases are transmitted, e.g., outbreak cluster, or weak community trnsmission). **The model's performance did not increase using transmission classification**.

## Acknowledgements

I thank WHO for making their data publically available.
