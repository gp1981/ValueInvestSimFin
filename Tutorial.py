# SimFin Tutorial from https://github.com/SimFin/simfin-tutorials/blob/master/01_Basics.ipynb
# 1) Create in VS code virtual environment venv
# 2) /.venv/Scripts/activate.bat
# 3) python -m pip install python-dotenv (for API Key management), pandas, matplotlib
# 4) run in the terminal cmd "python -m pip install simfin"
# 5) crate a file .env (starting with dot .) in the root of your project folder (not in /.venv)
# 6) open the file in VS code and include API_KEY=your API Key
# 7) run the following

import os
from dotenv import load_dotenv
from tqdm import tqdm


# Load API key from .env file in the root directory
load_dotenv()
API_KEY = os.environ.get('API_SIMFIN')

# 8) continue with the tutorial https://github.com/SimFin/simfin-tutorials/blob/master/01_Basics.ipynb

# matplotlib inline
import pandas as pd
import matplotlib as plt

# Import the main functionality from the SimFin Python API.
import simfin as sf

# Import names used for easy access to SimFin's data-columns.
from simfin.names import *

# Set the directory where the data is downloaded
sf.set_data_dir('~/simfin_data/')

# Replace YOUR_API_KEY with your actual API-key.
sf.set_api_key(api_key=API_KEY)

# Load data with sf.load
df1 = sf.load(dataset='income', variant='ttm', market='us', refresh_days=3)

# Display the first few rows of the DataFrame
print("\nDataFrame Head:")
print(df1.head())

num_rows, num_columns = df1.shape
print(f"Number of Rows: {num_rows}")
print(f"Number of Columns: {num_columns}")

# Display basic information about the DataFrame
print("DataFrame Info:")
print(df1.info())

# Display subset of data
print(df1.columns) 
selected_columns = ['Ticker','Fiscal Year','Fiscal Period','Operating Income (Loss)']
df1[selected_columns]
# The module names.py is auto-generated from definitions on the SimFin server. The SimFin website shows all of the column-names in the datasets where they belong, along with explanations of their meaning. The explanations are also noted in names.py

# Indexing dataframe
df2 = sf.load(dataset='income', variant='annual', market='us',
              index=[TICKER, REPORT_DATE],
              parse_dates=[REPORT_DATE, PUBLISH_DATE, RESTATED_DATE])
print(df2.head())

# Lookup Ticker, extract columns
df2.loc['MSFT']

selected_columns2 = ['Fiscal Year','Fiscal Period','Operating Income (Loss)']
df2.loc['MSFT'][selected_columns2]

# Plot
df2.loc['MSFT'][OPERATING_INCOME].plot(grid = True)

#  Load special function (financial statements)
df_income = sf.load_income(variant='ttm', market='us')
print(df_income.head())

df_balance = sf.load_balance(variant='ttm', market='us')
print(df_balance.columns)
print(df_balance.head())

df_cashflow = sf.load_cashflow(variant='ttm', market='us')
print(df_cashflow.columns)
print(df_cashflow.head())

# Report Date vs. Publish Date vs. Restated Date

# By default the functions sf.load_income(), sf.load_balance() and sf.load_cashflow() use the Report Date as an index, but it can be switched to use the Publish Date instead, by setting the index argument. We give a list of the indices we want in the resulting DataFrame, in this case we want both the Ticker and Publish Date.

df_income2 = sf.load_income(variant='ttm', market='us',
                            index=[TICKER, PUBLISH_DATE])
print(df_income2.head())


# Offset REPORT_DATE by 90 days
df_income3 = sf.add_date_offset(df=df_income,
                                date_index=REPORT_DATE,
                                offset=pd.DateOffset(days=90))
print(df_income3.head())

# Load latest price
df_prices_latest = sf.load_shareprices(variant='latest', market='us')
df_prices_latest.head()

# Load companies info
df_companies = sf.load_companies(index=TICKER, market='us')
print(df_companies.head())

# Load sector and industries
df_industries = sf.load_industries()
print(df_industries.head())
industry_id = df_companies.loc['MSFT'][INDUSTRY_ID]
df_industries.loc[industry_id]

# Dataset and columns name
sf.info_datasets()
sf.info_datasets('companies')
sf.info_columns(COMPANY_NAME)
sf.info_columns('shares')