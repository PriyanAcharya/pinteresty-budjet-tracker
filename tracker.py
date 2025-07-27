import pandas as pd
from db import init_db, add_expense, get_expenses
from utils import auto_category, should_treat_or_chill
from datetime import datetime
from rich.console import Console
from rich.table import Table

init_db()
console = Console()

def display_expenses():
    df = get_expenses()
    if df.empty:
        print("No expenses recorded yet.")
        return
    table = Table(title="💸 Pinterest-y Budget Tracker")

    for col in df.columns:
        table.add_column(col.capitalize(), style="magenta")
    for _, row in df.iterrows():
        table.add_row(*map(str, row.values))

    console.print(table)
    total = df['amount'].sum()
    console.print(f"\nTotal spent: ₹{total}", style="bold yellow")
    console.print(should_treat_or_chill(total), style="bold green")

def main():
    while True:
        print("\n1. Add Expense")
        print("2. Show All")
        print("3. Show Charts 📊")
        print("4. Exit")
        choice = input("Pick an option: ")

        if choice == '1':
            item = input("What did you spend on? ")
            amount = float(input("How much? ₹"))
            date = datetime.now().strftime("%Y-%m-%d")
            category = auto_category(item)
            add_expense(item, amount, category, date)
            print("✨ Expense added!\n")

        elif choice == '2':
            display_expenses()

        elif choice == '3':
            from visualize import pie_chart_by_category, bar_chart_over_time, line_plot_cumulative
            pie_chart_by_category()
            bar_chart_over_time()
            line_plot_cumulative()

        elif choice == '4':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
