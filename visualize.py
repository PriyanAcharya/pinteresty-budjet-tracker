import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from db import get_expenses

def generate_all_charts():
    df = get_expenses()
    if df.empty:
        return

    df['date'] = pd.to_datetime(df['date'])
    sns.set_theme(style="whitegrid", palette="pastel")

    # Pie chart
    pie_data = df.groupby('category')['amount'].sum()
    plt.figure(figsize=(6, 6))
    plt.pie(pie_data, labels=pie_data.index, autopct='%1.1ff%%', startangle=140)
    plt.title("Spending by Category")
    plt.tight_layout()
    plt.savefig("static/charts/pie.png")
    plt.close()

    # Bar chart
    bar_data = df.groupby('date')['amount'].sum().reset_index()
    plt.figure(figsize=(8, 4))
    sns.barplot(x='date', y='amount', data=bar_data, color='coral')
    plt.xticks(rotation=45)
    plt.title("Spending Over Time")
    plt.tight_layout()
    plt.savefig("static/charts/bar.png")
    plt.close()

    # Line chart
    df = df.sort_values('date')
    df['cumulative'] = df['amount'].cumsum()
    plt.figure(figsize=(8, 4))
    sns.lineplot(data=df, x='date', y='cumulative', marker="o", color="orchid")
    plt.title("Cumulative Spending Trend")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("static/charts/line.png")
    plt.close()
