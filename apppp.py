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
nearestday = duckdb.sql("""select MIN(days_to_maturity) AS days_to_maturity FROM df""")
nearestday = nearestday.to_df()
nearestday = nearestday['days_to_maturity'][0]
#print(type(nearestday))
#print("نزدیکترین سررسید:", nearestday)
st.write("نزدیکترین سررسید:", 'nearestday')
#گروه بندی دیتافریم بر اساس  روزهای مانده تا سررسید مورد نظز
gdf = df.groupby(df["days_to_maturity"])
days_striks = gdf.get_group(nearestday)

#days_striks.to_excel('nearest_striks.xlsx')

#استخراج نمادهایی که امروز سررسید میشن
stocklist = days_striks['ua_ticker'].values.tolist()

unique_list = list(set(stocklist))
#print(unique_list)
st.write(unique_list)

#گرفتن تاریخ شروع معاملات هر نماد و ذخیره کردن آن در لیست خود
for item in unique_list:
    start_date_df = days_striks.groupby(['ua_ticker'])
    itemsgrouped = start_date_df.get_group(item)
    start_date_list = itemsgrouped['begin_date'].values.tolist()
    #print(start_date_list)
    sorted_dates = sorted(start_date_list)
    #print(sorted_dates)
    unique_start_date_list = list(set(start_date_list))
    #print(item)
    st.write(item)
    first_item = sorted_dates[0]

    string_result = ''.join(first_item)
    original_date_str = str(string_result).strip()
    formatted_year = int(f"{string_result[:4]}")
    formated_month = int(f"{string_result[4:6]}")
    formated_day = int(f"{string_result[6:]}")
    shamsi = JalaliDate(date(formatted_year, formated_month, formated_day))
    #print(shamsi)
    st.write(shamsi)
