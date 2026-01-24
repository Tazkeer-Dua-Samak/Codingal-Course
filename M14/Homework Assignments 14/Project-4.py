import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("Company Sales Data.csv")
month_list = df['month_number'].tolist()
profit_list = df['total_profit'].tolist()

toothpaste_list = [sales for sales in df['toothpaste']]

def profit_line_chart():
    plt.plot(month_list, profit_list, marker='o', linestyle='-', color='blue')
    plt.title("Total Profit Graph")
    plt.xlabel("Month Number")
    plt.ylabel("Total Profit")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def toothpaste_scatter_chart():
    plt.scatter(month_list, toothpaste_list, color='green')
    plt.title("Toothpaste Sales Graph")
    plt.xlabel("Month Number")
    plt.ylabel("Number of units Sold")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

profit_line_chart()
toothpaste_scatter_chart()