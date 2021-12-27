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
percent = 'G:/My Drive/Stock_Market_Stuff/Stock_Images/volume_percent/'
data = 'G:/My Drive/Stock_Market_Stuff/Stock_Data/'
df = pd.read_csv(data + "master_data.csv")


all_tickers = list(set(chain(bonds, crypto, currency, basic_material, communication_services, consumer_cyclical, consumer_defensive, energy, financials, health, industrial, real_estate, technology, utilities, mix_bag, jag_resources, jag_renewable)))


dims = (100, 20)
fig, ax = plt.subplots(figsize=dims)


for stock in all_tickers:
    data = df[df['ticker'] == stock]

    fig = sns.lineplot(data=data, x='Date', y='Percent_Change_Volume', hue='ticker', legend = False)
    
    plt.tick_params(
    axis='both',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom=False,      # ticks along the bottom edge are off
    top=False,         # ticks along the top edge are off
    left=False,
    right=False,
    labelbottom=False,
    labeltop=False, # labels along the bottom edge are off
    labelleft=False,
    labelright=False
    ) 

    fig.figure.savefig(percent + stock + ".png")
    plt.clf()
    #plt.close('all')