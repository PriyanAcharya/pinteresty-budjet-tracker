from flask import Flask, render_template, request, redirect
from db import init_db, add_expense, get_expenses
from utils import auto_category, should_treat_or_chill
from visualize import generate_all_charts

app = Flask(__name__)
init_db()

@app.route('/')
def index():
    df = get_expenses()
    total = df['amount'].sum()
    recommendation = should_treat_or_chill(total)
    return render_template("index.html", expenses=df.to_dict(orient='records'),
                           total=total, recommendation=recommendation)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        item = request.form['item']
        amount = float(request.form['amount'])
        date = request.form['date']
        category = auto_category(item)
        add_expense(item, amount, category, date)
        generate_all_charts()
        return redirect('/')
    return render_template("add.html")

if __name__ == '__main__':
    app.run(debug=True)
