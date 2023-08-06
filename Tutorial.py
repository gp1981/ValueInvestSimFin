# SimFin Tutorial from https://github.com/SimFin/simfin-tutorials/blob/master/01_Basics.ipynb
# 1) Create in VS code virtual environment venv
# 2) /.venv/Scripts/activate.bat
# 3) python -m pip install python-dotenv (for API Key management)
# 4) run in the terminal cmd "python -m pip install simfin"
# 5) crate a file .env (starting with dot .) in the root of your project folder (not in /.venv)
# 6) open the file in VS code and include API_KEY=your API Key
# 7) run the following

import pandas
import matplotlib
import os
from dotenv import load_dotenv
from tqdm import tqdm

# Load API key from .env file in the root directory
load_dotenv()
API_KEY = os.environ.get('API_KEY')

# 8) continue with the tutorial https://github.com/SimFin/simfin-tutorials/blob/master/01_Basics.ipynb
