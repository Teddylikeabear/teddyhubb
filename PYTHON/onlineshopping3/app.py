from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from wtforms.fields.simple import FloatField

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'Teddylikeabear2703@'


db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    price = db.Column(db.Float, nullable=False)    

class CartItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product = db.relationship('Product', backref='cart_items')
    user = db.relationship('User', backref='cart_items')  

class Supplier(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

class SupplierRegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Register as Supplier')

class SupplierLoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login as Supplier')   

class ProductForm(FlaskForm):
    name = StringField('Product Name', validators=[DataRequired()])
    description = StringField('Product Description')
    price = FloatField('Product Price', validators=[DataRequired()])
    submit = SubmitField('Add Product')    


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user and user.password == password:
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('about'))
        else:
            flash('Invalid username or password. Please try again.', 'danger')

    return render_template('login.html')

"""
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))
"""

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', user=current_user)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        new_username = request.form['new_username']
        new_password = request.form['new_password']
        

        existing_user = User.query.filter_by(username=new_username).first()

        if existing_user:
            flash('Username already exists. Please choose a different username.', 'danger')
        else:
            new_user = User(username=new_username, password=new_password)
            db.session.add(new_user)
            db.session.commit()
            flash('Account created successfully! You can now log in.', 'success')
            return redirect(url_for('about'))

    return render_template('register.html')

@app.route('/about')
@login_required
def about():
    return render_template('about.html')

@app.route('/view_products')
def view_products():

    products = Product.query.all()
    return render_template('view_products.html', products=products)


@app.route('/cart')
def cart():
    cart_items = CartItem.query.filter_by(user_id=current_user.id).all()
    
    return render_template('cart.html', cart_items=cart_items)

@app.route('/update_quantity/<int:item_id>', methods=['POST'])
@login_required
def update_quantity(item_id):
    item = CartItem.query.get_or_404(item_id)
    new_quantity = int(request.form['quantity'])

    # Ensure the new quantity is valid (greater than 0)
    if new_quantity > 0:
        item.quantity = new_quantity
        db.session.commit()
        flash('Quantity updated successfully!', 'success')
    else:
        flash('Invalid quantity. Please enter a value greater than 0.', 'danger')

    return redirect(url_for('cart'))

@app.route('/delete_from_cart/<int:item_id>', methods=['POST'])
@login_required
def delete_from_cart(item_id):
    item = CartItem.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    flash('Item removed from the cart successfully!', 'success')
    return redirect(url_for('cart'))

@app.route('/account_settings')
def account_settings():
    
    return render_template('account_settings.html')

@app.route('/update_account_settings', methods=['POST'])
@login_required
def update_account_settings():
    new_username = request.form['new_username']
    new_password = request.form['new_password']

    current_user.username = new_username
    current_user.password = new_password

    db.session.commit()
    flash('Account settings updated successfully!', 'success')

    return redirect(url_for('account_settings'))

@app.route('/signout')
@login_required
def signout():
    logout_user()
    return render_template('signout.html')

@app.route('/register_supplier', methods=['GET', 'POST'])
def register_supplier():
    form = SupplierRegistrationForm()

    if form.validate_on_submit():
        
        new_supplier = Supplier(username=form.username.data, password=form.password.data)
        db.session.add(new_supplier)
        db.session.commit()
        flash('Supplier account created successfully!', 'success')
        return redirect(url_for('login')) 

    return render_template('register_supplier.html', form=form)

@app.route('/login_supplier', methods=['GET', 'POST'])
def login_supplier():
    form = SupplierLoginForm()

    if form.validate_on_submit():
        supplier = Supplier.query.filter_by(username=form.username.data).first()

        if supplier and supplier.check_password(form.password.data):
            login_user(supplier)
            flash('Login successful!', 'success')
            return redirect(url_for('supplier_dashboard'))

        flash('Invalid username or password. Please try again.', 'danger')

    return render_template('login_supplier.html', form=form)

@app.route('/supplier_dashboard')
@login_required
def supplier_dashboard():
    return render_template('supplier_dashboard.html')

@app.route('/add_product', methods=['GET', 'POST'])
@login_required
def add_product():
    form = ProductForm()

    if form.validate_on_submit():
       
        new_product = Product(name=form.name.data, description=form.description.data, price=form.price.data, supplier_id=current_user.id)
        db.session.add(new_product)
        db.session.commit()
        flash('Product added successfully!', 'success')
        return redirect(url_for('supplier_dashboard'))

    return render_template('add_product.html', form=form)

@app.route('/logout_supplier')
@login_required
def logout_supplier():
    logout_user()
    return redirect(url_for('index'))



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)



