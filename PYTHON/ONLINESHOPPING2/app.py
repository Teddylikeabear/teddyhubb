# app.py

from flask import Flask, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, current_user, logout_user
from forms import LoginForm
from models import User, Product, Cart, Order

app = Flask(__name__)
app.config['SECRET_KEY'] = 'teddylikeabear'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://teddyhubb:teddylikeabear@localhost/onlineshopping2'
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/')
def home():
    products = Product.query.all()
    return render_template('home.html', products=products)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password', 'danger')
    return render_template('login.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/add_to_cart/<int:product_id>')
@login_required
def add_to_cart(product_id):
    product = Product.query.get(product_id)
    if product:
        cart_item = Cart(user_id=current_user.id, product_id=product.id, quantity=1)
        db.session.add(cart_item)
        db.session.commit()
        flash('Item added to cart!', 'success')
    else:
        flash('Product not found!', 'danger')
    return redirect(url_for('home'))


@app.route('/cart')
@login_required
def view_cart():
    cart_items = Cart.query.filter_by(user_id=current_user.id).all()
    return render_template('shopping_cart.html', cart_items=cart_items)


@app.route('/checkout')
@login_required
def checkout():
    cart_items = Cart.query.filter_by(user_id=current_user.id).all()
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render_template('order_summary.html', cart_items=cart_items, total_price=total_price)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
