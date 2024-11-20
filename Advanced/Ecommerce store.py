"""
Simple eCommerce Website with Payment Processing using Stripe
------------------------------------------------------------

This project creates a simple eCommerce website that allows users to:
1. View products
2. Add them to the cart
3. Checkout and make payments using Stripe

Steps:
1. Set up Flask web server
2. Display products
3. Allow users to add products to their cart
4. Process payments via Stripe

Requirements:
- Flask (web server)
- Stripe (payment processing)
"""

import os
from flask import Flask, render_template, request, redirect, url_for, session
import stripe

# Initialize Flask app
app = Flask(__name__)

# Stripe API keys (replace these with your own keys)
stripe.api_key = 'sk_test_yourSecretKey'  # Secret Key
publishable_key = 'pk_test_yourPublishableKey'  # Publishable Key

# Product data (In a real application, this would come from a database)
products = [
    {'id': 1, 'name': 'Product 1', 'price': 10, 'description': 'Description for Product 1'},
    {'id': 2, 'name': 'Product 2', 'price': 20, 'description': 'Description for Product 2'},
    {'id': 3, 'name': 'Product 3', 'price': 30, 'description': 'Description for Product 3'},
]

# Set up the secret key for the session
app.secret_key = os.urandom(24)

@app.route('/')
def index():
    """
    Displays the list of products available in the store.
    """
    return render_template('index.html', products=products)

@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    """
    Adds the selected product to the shopping cart.
    """
    # Find the product by ID
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        # Add the product to the cart in the session
        if 'cart' not in session:
            session['cart'] = []
        session['cart'].append(product)
    return redirect(url_for('view_cart'))

@app.route('/cart')
def view_cart():
    """
    Displays the shopping cart with the products added.
    """
    cart = session.get('cart', [])
    total = sum(item['price'] for item in cart)
    return render_template('cart.html', cart=cart, total=total)

@app.route('/checkout')
def checkout():
    """
    Initiates the checkout process.
    """
    cart = session.get('cart', [])
    total = sum(item['price'] for item in cart)
    
    # Create a Stripe session for the payment
    checkout_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': item['name'],
                    'description': item['description']
                },
                'unit_amount': item['price'] * 100,  # Amount is in cents
            },
            'quantity': 1,
        } for item in cart],
        mode='payment',
        success_url=url_for('success', _external=True),
        cancel_url=url_for('cancel', _external=True),
    )

    return redirect(checkout_session.url, code=303)

@app.route('/success')
def success():
    """
    Displays a success message after a successful payment.
    """
    session.pop('cart', None)  # Clear the cart
    return render_template('success.html')

@app.route('/cancel')
def cancel():
    """
    Displays a cancel message if the payment is canceled.
    """
    return render_template('cancel.html')

if __name__ == '__main__':
    app.run(debug=True)
