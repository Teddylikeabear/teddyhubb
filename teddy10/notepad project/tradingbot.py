
import nasdaqdatalink
import pandas as pd
import quandl as qd


qd.ApiConfig.api_key = "bjKumHyVd-hMDgJkLfiM"
 
msft_data = qd.get("EOD/MSFT",
                   start_date="2010-01-01",
                   end_date="2010-09-01")
msft_data.head()

# Import numpy package
import numpy as np


# assign `Adj Close` to `close_price`
close_price = msft_data[['Adj_Close']]

# returns as fractional change
daily_return = close_price.pct_change()

# replacing NA values with 0
daily_return.fillna(0, inplace=True)

print(daily_return)

# assigning adjusted closing prices
# to adj_prices
adj_price = msft_data['Adj_Close']

# calculate the moving average
mav = adj_price.rolling(window=50).mean()

# print the result
print(mav[-10:])

# import the matplotlib package
# to see the plot
import matplotlib.pyplot as plt

adj_price.plot()

mav.plot()

# import the matplotlib package
# to see the plot
import matplotlib.pyplot as plt

adj_price.plot()
mav.plot()

