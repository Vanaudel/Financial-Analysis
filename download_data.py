import pandas as pd
import datetime
import numpy as np
from time import sleep

import matplotlib.pyplot as plt
import seaborn as sns

import yfinance as yf
from itertools import chain

from tickers import bonds, crypto, currency, basic_material, communication_services, consumer_cyclical, consumer_defensive, energy, financials, health, industrial, real_estate, technology, utilities, mix_bag, jag_resources, jag_renewable


desktop = '/Users/jagpaul/Desktop/Results/' #set to folder on your desktop
gd = 'G:/My Drive/Stock_Market_Stuff/Stock_Data/'


def select_stock(stock):
    ticker = yf.Ticker(stock)
    df = ticker.history(period="1095d").reset_index()
    df['ticker'] = stock
    
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    df = df.resample('D').ffill().reset_index() #fills in the weekends and holidays
    
    df['Percent_Change_Open'] = df['Open'].pct_change()
    df['Percent_Change_High'] = df['High'].pct_change()
    df['Percent_Change_Low'] = df['Low'].pct_change()
    df['Percent_Change_Close'] = df['Close'].pct_change()
    df['Percent_Change_Volume'] = df['Volume'].pct_change()

    df['closing_moving_average_7d'] = df['Close'].rolling(window=7).mean()
    df['closing_moving_average_14d'] = df['Close'].rolling(window=14).mean()
    df['closing_moving_average_21d'] = df['Close'].rolling(window=21).mean()
    df['closing_moving_average_28d'] = df['Close'].rolling(window=28).mean()
    df['closing_moving_average_35d'] = df['Close'].rolling(window=35).mean()
    df['closing_moving_average_42d'] = df['Close'].rolling(window=42).mean()
    df['closing_moving_average_49d'] = df['Close'].rolling(window=49).mean()
    df['closing_moving_average_50d'] = df['Close'].rolling(window=50).mean()
    df['closing_moving_average_56d'] = df['Close'].rolling(window=56).mean()
    df['closing_moving_average_63d'] = df['Close'].rolling(window=63).mean()
    df['closing_moving_average_70d'] = df['Close'].rolling(window=70).mean()
    df['closing_moving_average_77d'] = df['Close'].rolling(window=77).mean()
    df['closing_moving_average_84d'] = df['Close'].rolling(window=84).mean()
    df['closing_moving_average_91d'] = df['Close'].rolling(window=91).mean()
    df['closing_moving_average_98d'] = df['Close'].rolling(window=98).mean()
    df['closing_moving_average_105d'] = df['Close'].rolling(window=105).mean()
    df['closing_moving_average_112d'] = df['Close'].rolling(window=112).mean()
    df['closing_moving_average_119d'] = df['Close'].rolling(window=119).mean()
    df['closing_moving_average_126d'] = df['Close'].rolling(window=126).mean()
    df['closing_moving_average_133d'] = df['Close'].rolling(window=133).mean()
    df['closing_moving_average_140d'] = df['Close'].rolling(window=140).mean()
    df['closing_moving_average_147d'] = df['Close'].rolling(window=147).mean()
    df['closing_moving_average_154d'] = df['Close'].rolling(window=154).mean()
    df['closing_moving_average_161d'] = df['Close'].rolling(window=161).mean()
    df['closing_moving_average_168d'] = df['Close'].rolling(window=168).mean()
    df['closing_moving_average_175d'] = df['Close'].rolling(window=175).mean()
    df['closing_moving_average_182d'] = df['Close'].rolling(window=182).mean()
    df['closing_moving_average_189d'] = df['Close'].rolling(window=189).mean()
    df['closing_moving_average_196d'] = df['Close'].rolling(window=196).mean()
    df['closing_moving_average_200d'] = df['Close'].rolling(window=200).mean()
    df['closing_moving_average_203d'] = df['Close'].rolling(window=203).mean()
    df['closing_moving_average_210d'] = df['Close'].rolling(window=210).mean()
    df['closing_moving_average_217d'] = df['Close'].rolling(window=217).mean()
    df['closing_moving_average_224d'] = df['Close'].rolling(window=224).mean()

    df['cross_50_200'] = np.where(df['closing_moving_average_50d'] > df['closing_moving_average_200d'], 'GOLDEN', 'DEATH')

    
    df = df.tail(1095) #Since countries have different holidays, the ffill wont be the same for each ticker. You have to take the last 'n' entries for each ticker to align them.
    return df


from itertools import chain
all_tickers = list(set(chain(bonds, crypto, currency, basic_material, communication_services, consumer_cyclical, consumer_defensive, energy, financials, health, industrial, real_estate, technology, utilities, mix_bag, jag_resources, jag_renewable)))



untouched_data = []

for ticker in all_tickers: #select list from tickers module
    df = select_stock(ticker)
    untouched_data.append(df)

untouched_data_df = pd.concat(untouched_data, ignore_index=True)
untouched_data_df.to_csv(gd + 'master_data.csv', encoding='utf-8')