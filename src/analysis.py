import numpy as np

def analyze_data(df):

    monthly_sales = df.groupby(df['Date'].dt.month)['Revenue'].sum()

    top_products = df.groupby('Product')['Revenue'].sum().sort_values(ascending=False)

    region_sales = df.groupby('Region')['Revenue'].sum()

    total_profit = df['Profit'].sum()

    mean_sales = np.mean(df['Revenue'])
    median_sales = np.median(df['Revenue'])

    return {
        "monthly_sales": monthly_sales,
        "top_products": top_products,
        "region_sales": region_sales,
        "total_profit": total_profit,
        "mean_sales": mean_sales,
        "median_sales": median_sales
    }