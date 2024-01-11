from flask import Flask, render_template, session, request, url_for, redirect

app = Flask(__name__)
app.secret_key = 'teddylikeabear'  # Change this to a secure random key

# Sample product data (replace this with a database)
products = [
    {'id': 1, 'name': 'Product 1', 'price': 1500.0, 'image': 'product1.jpg'},
    {'id': 2, 'name': 'Product 2', 'price': 120.0, 'image': 'product2.jpg'},
    {'id': 3, 'name': 'Product 3', 'price': 700.0, 'image': 'product3.jpg'},
]

@app.route('/')
def home():
    team_members = [
        {'name': 'Thendo Charmaine Marageni', 'position': 'CEO', 'bio': ' FOUNDER'},
        
        
    ]

    milestones = [
        {'year': '2020', 'event': 'Company founded', 'description': ' infinitt'},
      
    ]
    return render_template('home.html' , team_members=team_members, milestones=milestones)

@app.route('/products')
def product_list():
    return render_template('products.html', products=products)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        return render_template('product.html', product=product)
    return redirect(url_for('product_list'))

@app.route('/cart')
def view_cart():
    cart = session.get('cart', [])
    total_price = sum(item['price'] for item in cart)
    return render_template('cart.html', cart=cart, total_price=total_price)

@app.route('/add_to_cart/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        cart = session.get('cart', [])
        cart.append({'id': product['id'], 'name': product['name'], 'price': product['price']})
        session['cart'] = cart
    return redirect(url_for('product_list'))

@app.route('/remove_from_cart/<int:product_id>', methods=['POST'])
def remove_from_cart(product_id):
    # Logic to remove the product from the cart
   cart = session.get('cart', [])
   cart = [item for item in cart if item['id'] != product_id]
   session['cart'] = cart
   return redirect(url_for('view_cart'))


@app.route('/checkout',methods=['GET', 'POST'])
def checkout():

     if request.method == 'POST':
        session.pop('cart', None) #this will clear cart after checkout
        return redirect(url_for('view_cart'))

     return render_template('checkout.html')       

if __name__ == '__main__':
    app.run(debug=True)
