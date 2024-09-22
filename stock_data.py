import yfinance as yf
 

def yfinance_stock_data(ticker: str, period ="max"):
    company = yf.Ticker(ticker)

    # Store stock history in a Pandas dataframe. 
    data = company.history(period)
    data.reset_index(inplace=True)

    # Return the first five rows in the Pandas dataframe. 
    return data.tail()


# Extract Tesla stock data using yfinance.
tesla_stock = yfinance_stock_data('TSLA')
print(tesla_stock)

# Extract GameStop stock data using yfinance.
gamestop_stock = yfinance_stock_data('GME')
print(gamestop_stock)
