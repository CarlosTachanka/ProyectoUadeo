from flask import current_app as app
from flask import render_template, request, redirect, url_for
from .models import User, Product, db

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        if name and email:
            new_user = User(name=name, email=email)
            try:
                db.session.add(new_user)
                db.session.commit()
            except:
                db.session.rollback()
        return redirect(url_for('users'))
    
    all_users = User.query.all()
    return render_template('users.html', users=all_users)

@app.route('/products', methods=['GET', 'POST'])
def products():
    if request.method == 'POST':
        name = request.form.get('name')
        price = request.form.get('price')
        stock = request.form.get('stock')
        if name and price:
            new_product = Product(name=name, price=float(price), stock=int(stock or 0))
            try:
                db.session.add(new_product)
                db.session.commit()
            except:
                db.session.rollback()
        return redirect(url_for('products'))
    
    all_products = Product.query.all()
    return render_template('products.html', products=all_products)
