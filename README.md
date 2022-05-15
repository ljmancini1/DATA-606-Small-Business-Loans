# State Small Business Credit Initiative

This repo contains code for the purpose of creating a predictive model that predicts the ability of a small business to create jobs as a result of financing directly or indirectly tied to the SSBCI.

### Datasets

In the `data` folder there are several `.csvs` used in the code

- `SSBCI Transaction Data.csv` - this is the data directly taken from the US Treasury departments website with the information gathered about the first implementation of the SSBCI from 2010-2017. It can be download directly from here [SSBCI Transaction Data](https://home.treasury.gov/system/files/256/SSBCI-Transactions-Dataset.csv) and data definitions can be found here [SSBCI Data Definitions](https://home.treasury.gov/system/files/256/SSBCI-Data-Definitions.pdf).
- `SSBCI_One_Hot.csv` - preprocessed data export from `DataPreprocessing.ipynb` that has categorical columns One-Hot encoded
- `SSBCI_data.csv` - preprocessed data export from `DataPreprocessing.ipynb` that is categorically encoded with `LabelEncoder()`
- `ssbci_catdata.csv` - preprocessed data export frome `DataPreprocessing.ipynb` that retains the `str` based categories
- `unemployment2009-2018.csv` - US Unemployment Rate by month from 2009-2018 used as a feature in model creation
