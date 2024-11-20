"""
Personal Finance Manager with Machine Learning Integration
---------------------------------------------------------
This script allows users to input their income, expenses, and investments,
and analyze their spending behavior. It also predicts future expenses using machine learning.

Libraries:
- Flask for web server
- SQLite for database storage
- Pandas for data analysis
- scikit-learn for expense prediction (Linear Regression)

Steps:
1. Collect data on transactions (income, expense, investments).
2. Store data in SQLite database.
3. Analyze data and visualize spending.
4. Use machine learning to predict future expenses.
"""

import sqlite3
from flask import Flask, request, render_template_string
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Create SQLite database to store transactions
def create_db():
    conn = sqlite3.connect('finance.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS transactions
                 (date TEXT, category TEXT, amount REAL)''')
    conn.commit()
    conn.close()

# Store transaction in the database
def add_transaction(date, category, amount):
    conn = sqlite3.connect('finance.db')
    c = conn.cursor()
    c.execute('INSERT INTO transactions (date, category, amount) VALUES (?, ?, ?)',
              (date, category, amount))
    conn.commit()
    conn.close()

# Predict future expenses based on historical data using Linear Regression
def predict_expenses():
    conn = sqlite3.connect('finance.db')
    c = conn.cursor()
    c.execute('SELECT date, amount FROM transactions WHERE category = "Expense"')
    data = c.fetchall()
    conn.close()

    # Convert the data to a pandas DataFrame for analysis
    df = pd.DataFrame(data, columns=["date", "amount"])
    df["date"] = pd.to_datetime(df["date"])
    df["date_int"] = (df["date"] - df["date"].min()).dt.days

    # Prepare the data for training the model
    X = df["date_int"].values.reshape(-1, 1)
    y = df["amount"].values

    # Fit Linear Regression model
    model = LinearRegression()
    model.fit(X, y)

    # Predict future expense for the next 7 days
    future_dates = np.array([df["date_int"].max() + i for i in range(1, 8)]).reshape(-1, 1)
    predicted_expenses = model.predict(future_dates)

    return predicted_expenses

# Flask route to add transaction
@app.route('/add_transaction', methods=['POST'])
def add_transaction_route():
    date = request.form['date']
    category = request.form['category']
    amount = float(request.form['amount'])
    add_transaction(date, category, amount)
    return "Transaction Added!"

# Flask route to view prediction
@app.route('/predict_expenses', methods=['GET'])
def predict_expenses_route():
    predicted_expenses = predict_expenses()
    prediction_message = f"Predicted expenses for the next 7 days: {predicted_expenses}"
    return prediction_message

# Flask route to display transactions
@app.route('/view_transactions', methods=['GET'])
def view_transactions_route():
    conn = sqlite3.connect('finance.db')
    c = conn.cursor()
    c.execute('SELECT * FROM transactions')
    transactions = c.fetchall()
    conn.close()

    html = "<h1>Transactions</h1><table><tr><th>Date</th><th>Category</th><th>Amount</th></tr>"
    for transaction in transactions:
        html += f"<tr><td>{transaction[0]}</td><td>{transaction[1]}</td><td>{transaction[2]}</td></tr>"
    html += "</table>"
    return html

# Main function to start Flask app
if __name__ == '__main__':
    create_db()
    app.run(debug=True)
