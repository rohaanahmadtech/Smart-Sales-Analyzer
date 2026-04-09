import matplotlib.pyplot as plt
import os

os.makedirs("outputs/charts", exist_ok=True)

def plot_monthly_sales(df):
    monthly_sales = df.groupby(df['Date'].dt.month)['Revenue'].sum()

    plt.figure()
    monthly_sales.plot()

    plt.title("Monthly Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Revenue")

    plt.savefig("outputs/charts/monthly_sales.png")
    plt.close()


def plot_top_products(df):
    top_products = df.groupby('Product')['Revenue'].sum().sort_values(ascending=False)

    plt.figure()
    top_products.plot(kind='bar')

    plt.title("Top Selling Products")
    plt.xlabel("Product")
    plt.ylabel("Revenue")

    plt.savefig("outputs/charts/top_products.png")
    plt.close()


def plot_category_distribution(df):
    category_sales = df.groupby('Category')['Revenue'].sum()

    plt.figure()
    category_sales.plot(kind='pie', autopct='%1.1f%%')

    plt.title("Category Distribution")

    plt.savefig("outputs/charts/category_distribution.png")
    plt.close()


def plot_profit_analysis(df):
    profit = df['Profit'].sum()
    cost = df['Cost_Total'].sum()

    labels = ['Profit', 'Cost']
    values = [profit, cost]

    plt.figure()
    plt.bar(labels, values)

    plt.title("Profit vs Cost")

    plt.savefig("outputs/charts/profit_analysis.png")
    plt.close()

def create_charts(df):
    plot_monthly_sales(df)
    plot_top_products(df)
    plot_category_distribution(df)
    plot_profit_analysis(df)