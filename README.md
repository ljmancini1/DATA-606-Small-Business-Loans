# State Small Business Credit Initiative

This repo contains code for the purpose of creating a predictive model that predicts the ability of a small business to create jobs as a result of financing directly or indirectly tied to the SSBCI.

### Datasets

In the `data` folder there are several `.csvs` used in the code

- `SSBCI Transaction Data.csv` - this is the data directly taken from the US Treasury departments website with the information gathered about the first implementation of the SSBCI from 2010-2017. It can be download directly from here [SSBCI Transaction Data](https://home.treasury.gov/system/files/256/SSBCI-Transactions-Dataset.csv) and data definitions can be found here [SSBCI Data Definitions](https://home.treasury.gov/system/files/256/SSBCI-Data-Definitions.pdf).
- `SSBCI_One_Hot.csv` - preprocessed data export from `DataPreprocessing.ipynb` that has categorical columns One-Hot encoded
- `SSBCI_data.csv` - preprocessed data export from `DataPreprocessing.ipynb` that is categorically encoded with `LabelEncoder()`
- `ssbci_catdata.csv` - preprocessed data export frome `DataPreprocessing.ipynb` that retains the `str` based categories
- `unemployment2009-2018.csv` - US Unemployment Rate by month from 2009-2018 used as a feature in model creation

### Clustering

This contains all the code for creating a K-Prototypes clustering model and visualizing the clusters using Uniform Manifold Approximation. It also creates a dataset called `ssbci_datawithclusters.csv` which appends the assigned cluster from K-Prototypes to the feature vector.

### Classification and Regresssion

Several classification techniques are compared to see if which performs better in binary classification. Classification is based on predicting whether or not jobs were created. `creation_status = {1,0}` represents the label for the feature vector.

> **jobs_created** - The number of new Full-Time Equivalent jobs expected to be created as a direct result of the loan or investment. These jobs must be expected to materialize in no more than 2 years from the date of the loan or investment closing.

Regression uses and OLS multiple linear regression model to try to predict how many jobs a company may create as a result of SSBCI financing

### API

Run the api.py file to create a locally running RESTapi that will take one or many feature vectors in json format and will output a prediction for whether or not a company will create jobs as a result of financing. This can be used to adjust financing levels to predict multiple outcomes for a company. Based on the Gradient Boosting Classification model found in `Classification and Regression.ipynb`. 

Example input:
`[   { "loan_investment_amount": 1, "ssbci_original_funds": 1, "full_time_employees" : 1, "revenue": 1, "jobs_retained": 1,  "SPY_Close": 1}
 ]`
