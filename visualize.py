import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from db import get_expenses

sns.set_theme(style="whitegrid", palette="pastel")

def pie_chart_by_category():
    df = get_expenses()
    if df.empty:
        print("No data to plot.")
        return
    category_totals = df.groupby('category')['amount'].sum()
    colors = sns.color_palette('pastel')[0:len(category_totals)]
    
    plt.figure(figsize=(8, 6))
    plt.pie(category_totals, labels=category_totals.index, colors=colors, autopct='%1.1f%%')
    plt.title("Spending by Category 💸")
    plt.show()

def bar_chart_over_time():
    df = get_expenses()
    if df.empty:
        print("No data to plot.")
        return
    df['date'] = pd.to_datetime(df['date'])
    df_grouped = df.groupby('date')['amount'].sum().reset_index()

    plt.figure(figsize=(10, 5))
    sns.barplot(x='date', y='amount', data=df_grouped, color='coral')
    plt.xticks(rotation=45)
    plt.title("Spending Over Time 📅")
    plt.ylabel("Amount (₹)")
    plt.tight_layout()
    plt.show()

def line_plot_cumulative():
    df = get_expenses()
    if df.empty:
        print("No data to plot.")
        return
    df['date'] = pd.to_datetime(df['date'])
    df_sorted = df.sort_values('date')
    df_sorted['cumulative'] = df_sorted['amount'].cumsum()

    plt.figure(figsize=(10, 5))
    sns.lineplot(data=df_sorted, x='date', y='cumulative', marker="o", color="mediumorchid")
    plt.title("Cumulative Spending Trend 📈")
    plt.ylabel("Total Spent (₹)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
