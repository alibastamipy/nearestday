#developing code
import streamlit as st
from IPython.display import display
import pandas as pd
import duckdb
from tseopt import get_all_options_data
import numpy as np
from datetime import datetime
import openpyxl
from datetime import date, datetime
from khayyam import JalaliDate, JalaliDatetime, TehranTimezone
#import warnings
#warnings.filterwarnings('ignore')

days = int(input("Days To Maturity:"))

entire_option_market_data = get_all_options_data()
#ذخیره دیتای گرفته شده در دیتافریم پانداس
df = pd.DataFrame(entire_option_market_data)
st.write(df)
