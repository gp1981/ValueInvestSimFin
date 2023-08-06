# SimFin Tutorial from https://github.com/SimFin/simfin-tutorials/blob/master/01_Basics.ipynb
# 1) Create in VS code virtual environment venv
# 2) /.venv/Scripts/activate.bat
# 3) python -m pip install python-dotenv (for API Key management)
# 4) run in the terminal cmd "python -m pip install simfin"
# 5) crate a file .env (starting with dot .) in the root of your project folder (not in /.venv)
# 6) open the file in VS code and include API_KEY=your API Key
# 7) run the following

import os
from dotenv import load_dotenv
from tqdm import tqdm

# Load API key from .env file in the root directory
load_dotenv()
API_KEY = os.environ.get('API_KEY')

# 8) continue with the tutorial https://github.com/SimFin/simfin-tutorials/blob/master/01_Basics.ipynb

# matplotlib inline
import pandas as pd

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

# Check the data download, get the size and an overview
df1.head()
num_rows, num_columns = df1.shape
print(f"Number of Rows: {num_rows}")
print(f"Number of Columns: {num_columns}")

# Display basic information about the DataFrame
print("DataFrame Info:")
print(df1.info())

# Display the first few rows of the DataFrame
print("\nDataFrame Head:")
print(df1.head())

# Display subset of data
