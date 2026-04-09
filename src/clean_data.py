import pandas as pd

def clean_data(df):
    df = df.drop_duplicates()
    df = df.dropna()

    df['Date'] = pd.to_datetime(df['Date'])

    df['Revenue'] = df['Quantity'] * df['Price']
    df['Cost_Total'] = df['Quantity'] * df['Cost']
    df['Profit'] = df['Revenue'] - df['Cost_Total']

    return df