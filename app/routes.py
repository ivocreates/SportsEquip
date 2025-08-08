from flask import Blueprint, render_template, redirect, url_for, flash, request, jsonify
from flask_login import login_user, logout_user, login_required, current_user
from app import db
from app.models import User, Product, Order, OrderItem, CartItem, Review, Wishlist
from app.forms import LoginForm, RegistrationForm, ProductForm, ReviewForm, UpdateOrderStatusForm
from datetime import datetime

main = Blueprint('main', __name__)

# Home page
@main.route('/')
def index():
    featured_products = Product.query.limit(8).all()
    return render_template('index.html', products=featured_products)

# Authentication routes
@main.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            next_page = request.args.get('next')
            if user.is_admin:
                return redirect(next_page) if next_page else redirect(url_for('main.admin_dashboard'))
            return redirect(next_page) if next_page else redirect(url_for('main.index'))
        flash('Invalid email or password', 'danger')
    return render_template('auth/login.html', form=form)

@main.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    
    form = RegistrationForm()
    if form.validate_on_submit():
        # Check if user already exists
        if User.query.filter_by(email=form.email.data).first():
            flash('Email already registered', 'danger')
            return render_template('auth/register.html', form=form)
        
        if User.query.filter_by(username=form.username.data).first():
            flash('Username already taken', 'danger')
            return render_template('auth/register.html', form=form)
        
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Registration successful!', 'success')
        return redirect(url_for('main.login'))
    return render_template('auth/register.html', form=form)

@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))

# Product routes
@main.route('/products')
def products():
    page = request.args.get('page', 1, type=int)
    category = request.args.get('category')
    search = request.args.get('search')
    
    query = Product.query
    
    if category:
        query = query.filter_by(category=category)
    
    if search:
        query = query.filter(Product.name.contains(search))
    
    products = query.paginate(
        page=page, per_page=12, error_out=False
    )
    
    categories = db.session.query(Product.category).distinct().all()
    categories = [cat[0] for cat in categories]
    
    return render_template('products/products.html', products=products, categories=categories)

@main.route('/product/<int:id>')
def product_detail(id):
    product = Product.query.get_or_404(id)
    reviews = Review.query.filter_by(product_id=id).all()
    form = ReviewForm()
    return render_template('products/product_detail.html', product=product, reviews=reviews, form=form)

# Cart routes
@main.route('/add-to-cart', methods=['POST'])
@login_required
def add_to_cart():
    product_id = request.form.get('product_id')
    quantity = int(request.form.get('quantity', 1))
    
    product = Product.query.get_or_404(product_id)
    
    if product.stock_quantity < quantity:
        flash('Not enough stock available', 'danger')
        return redirect(url_for('main.product_detail', id=product_id))
    
    cart_item = CartItem.query.filter_by(user_id=current_user.id, product_id=product_id).first()
    
    if cart_item:
        cart_item.quantity += quantity
    else:
        cart_item = CartItem(user_id=current_user.id, product_id=product_id, quantity=quantity)
        db.session.add(cart_item)
    
    db.session.commit()
    flash('Item added to cart!', 'success')
    return redirect(url_for('main.product_detail', id=product_id))

@main.route('/cart')
@login_required
def cart():
    cart_items = CartItem.query.filter_by(user_id=current_user.id).all()
    total = sum(item.product.price * item.quantity for item in cart_items)
    return render_template('cart/cart.html', cart_items=cart_items, total=total)

@main.route('/remove-from-cart/<int:id>')
@login_required
def remove_from_cart(id):
    cart_item = CartItem.query.get_or_404(id)
    if cart_item.user_id == current_user.id:
        db.session.delete(cart_item)
        db.session.commit()
        flash('Item removed from cart', 'success')
    return redirect(url_for('main.cart'))

@main.route('/add-all-to-cart', methods=['POST'])
@login_required
def add_all_to_cart():
    wishlist_items = Wishlist.query.filter_by(user_id=current_user.id).all()
    
    if not wishlist_items:
        flash('Your wishlist is empty', 'warning')
        return redirect(url_for('main.wishlist'))
    
    added_count = 0
    for wishlist_item in wishlist_items:
        product = wishlist_item.product
        
        # Check if product has stock
        if product.stock_quantity > 0:
            # Check if item already in cart
            cart_item = CartItem.query.filter_by(user_id=current_user.id, product_id=product.id).first()
            
            if cart_item:
                # Add 1 more to existing cart item if stock allows
                if product.stock_quantity > cart_item.quantity:
                    cart_item.quantity += 1
                    added_count += 1
            else:
                # Add new item to cart
                cart_item = CartItem(user_id=current_user.id, product_id=product.id, quantity=1)
                db.session.add(cart_item)
                added_count += 1
    
    if added_count > 0:
        db.session.commit()
        flash(f'{added_count} items added to cart from wishlist!', 'success')
    else:
        flash('No items could be added to cart (out of stock or already in cart)', 'warning')
    
    return redirect(url_for('main.wishlist'))

@main.route('/cart-count')
@login_required
def cart_count():
    count = CartItem.query.filter_by(user_id=current_user.id).count()
    return jsonify({'count': count})

# Order routes
@main.route('/checkout', methods=['POST'])
@login_required
def checkout():
    cart_items = CartItem.query.filter_by(user_id=current_user.id).all()
    
    if not cart_items:
        flash('Your cart is empty', 'warning')
        return redirect(url_for('main.cart'))
    
    total = sum(item.product.price * item.quantity for item in cart_items)
    
    # Create order
    order = Order(user_id=current_user.id, total_amount=total)
    db.session.add(order)
    db.session.flush()  # Get the order ID
    
    # Create order items and update stock
    for cart_item in cart_items:
        order_item = OrderItem(
            order_id=order.id,
            product_id=cart_item.product_id,
            quantity=cart_item.quantity,
            price=cart_item.product.price
        )
        db.session.add(order_item)
        
        # Update product stock
        cart_item.product.stock_quantity -= cart_item.quantity
        
        # Remove from cart
        db.session.delete(cart_item)
    
    db.session.commit()
    flash('Order placed successfully!', 'success')
    return redirect(url_for('main.orders'))

@main.route('/orders')
@login_required
def orders():
    user_orders = Order.query.filter_by(user_id=current_user.id).order_by(Order.created_at.desc()).all()
    return render_template('orders/orders.html', orders=user_orders)

# Review routes
@main.route('/add-review', methods=['POST'])
@login_required
def add_review():
    form = ReviewForm()
    if form.validate_on_submit():
        # Check if user has already reviewed this product
        existing_review = Review.query.filter_by(
            user_id=current_user.id, 
            product_id=form.product_id.data
        ).first()
        
        if existing_review:
            flash('You have already reviewed this product', 'warning')
        else:
            review = Review(
                user_id=current_user.id,
                product_id=form.product_id.data,
                rating=form.rating.data,
                comment=form.comment.data
            )
            db.session.add(review)
            db.session.commit()
            flash('Review added successfully!', 'success')
    
    return redirect(url_for('main.product_detail', id=form.product_id.data))

# Wishlist routes
@main.route('/add-to-wishlist/<int:product_id>')
@login_required
def add_to_wishlist(product_id):
    product = Product.query.get_or_404(product_id)
    
    existing = Wishlist.query.filter_by(user_id=current_user.id, product_id=product_id).first()
    if existing:
        flash('Item already in wishlist', 'info')
    else:
        wishlist_item = Wishlist(user_id=current_user.id, product_id=product_id)
        db.session.add(wishlist_item)
        db.session.commit()
        flash('Item added to wishlist!', 'success')
    
    return redirect(url_for('main.product_detail', id=product_id))

@main.route('/wishlist')
@login_required
def wishlist():
    wishlist_items = Wishlist.query.filter_by(user_id=current_user.id).all()
    return render_template('wishlist/wishlist.html', wishlist_items=wishlist_items)

@main.route('/remove-from-wishlist/<int:id>')
@login_required
def remove_from_wishlist(id):
    wishlist_item = Wishlist.query.get_or_404(id)
    if wishlist_item.user_id == current_user.id:
        db.session.delete(wishlist_item)
        db.session.commit()
        flash('Item removed from wishlist', 'success')
    return redirect(url_for('main.wishlist'))

# Admin routes
@main.route('/admin')
@login_required
def admin_dashboard():
    if not current_user.is_admin:
        flash('Access denied', 'danger')
        return redirect(url_for('main.index'))
    
    total_products = Product.query.count()
    total_orders = Order.query.count()
    total_users = User.query.filter_by(is_admin=False).count()
    pending_orders = Order.query.filter_by(status='pending').count()
    
    recent_orders = Order.query.order_by(Order.created_at.desc()).limit(5).all()
    
    return render_template('admin/dashboard.html', 
                         total_products=total_products,
                         total_orders=total_orders,
                         total_users=total_users,
                         pending_orders=pending_orders,
                         recent_orders=recent_orders)

@main.route('/admin/products')
@login_required
def admin_products():
    if not current_user.is_admin:
        flash('Access denied', 'danger')
        return redirect(url_for('main.index'))
    
    page = request.args.get('page', 1, type=int)
    products = Product.query.paginate(page=page, per_page=10, error_out=False)
    return render_template('admin/products.html', products=products)

@main.route('/admin/products/add', methods=['GET', 'POST'])
@login_required
def admin_add_product():
    if not current_user.is_admin:
        flash('Access denied', 'danger')
        return redirect(url_for('main.index'))
    
    form = ProductForm()
    if form.validate_on_submit():
        product = Product(
            name=form.name.data,
            description=form.description.data,
            price=form.price.data,
            category=form.category.data,
            image_url=form.image_url.data or 'default-product.jpg',
            stock_quantity=form.stock_quantity.data
        )
        db.session.add(product)
        db.session.commit()
        flash('Product added successfully!', 'success')
        return redirect(url_for('main.admin_products'))
    
    return render_template('admin/add_product.html', form=form)

@main.route('/admin/products/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def admin_edit_product(id):
    if not current_user.is_admin:
        flash('Access denied', 'danger')
        return redirect(url_for('main.index'))
    
    product = Product.query.get_or_404(id)
    form = ProductForm(obj=product)
    
    if form.validate_on_submit():
        product.name = form.name.data
        product.description = form.description.data
        product.price = form.price.data
        product.category = form.category.data
        product.image_url = form.image_url.data or 'default-product.jpg'
        product.stock_quantity = form.stock_quantity.data
        db.session.commit()
        flash('Product updated successfully!', 'success')
        return redirect(url_for('main.admin_products'))
    
    return render_template('admin/edit_product.html', form=form, product=product)

@main.route('/admin/products/delete/<int:id>')
@login_required
def admin_delete_product(id):
    if not current_user.is_admin:
        flash('Access denied', 'danger')
        return redirect(url_for('main.index'))
    
    product = Product.query.get_or_404(id)
    
    # Check if product has been ordered (prevent deletion if it's part of existing orders)
    if product.order_items:
        flash('Cannot delete product that has been ordered. Consider marking it as out of stock instead.', 'warning')
        return redirect(url_for('main.admin_products'))
    
    try:
        # Delete related records first
        # Delete cart items
        CartItem.query.filter_by(product_id=id).delete()
        
        # Delete reviews
        Review.query.filter_by(product_id=id).delete()
        
        # Delete wishlist items
        Wishlist.query.filter_by(product_id=id).delete()
        
        # Finally delete the product
        db.session.delete(product)
        db.session.commit()
        flash('Product deleted successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash('Error deleting product. Please try again.', 'danger')
    
    return redirect(url_for('main.admin_products'))

@main.route('/admin/orders')
@login_required
def admin_orders():
    if not current_user.is_admin:
        flash('Access denied', 'danger')
        return redirect(url_for('main.index'))
    
    page = request.args.get('page', 1, type=int)
    orders = Order.query.order_by(Order.created_at.desc()).paginate(
        page=page, per_page=10, error_out=False
    )
    return render_template('admin/orders.html', orders=orders)

@main.route('/admin/orders/<int:id>/update-status', methods=['POST'])
@login_required
def admin_update_order_status(id):
    if not current_user.is_admin:
        flash('Access denied', 'danger')
        return redirect(url_for('main.index'))
    
    order = Order.query.get_or_404(id)
    form = UpdateOrderStatusForm()
    
    if form.validate_on_submit():
        order.status = form.status.data
        db.session.commit()
        flash('Order status updated successfully!', 'success')
    
    return redirect(url_for('main.admin_orders'))

# Support and Company Pages
@main.route('/help-center')
def help_center():
    return render_template('support/help_center.html')

@main.route('/contact-us')
def contact_us():
    return render_template('support/contact_us.html')

@main.route('/shipping-info')
def shipping_info():
    return render_template('support/shipping_info.html')

@main.route('/returns')
def returns():
    return render_template('support/returns.html')

@main.route('/about-us')
def about_us():
    return render_template('company/about_us.html')

@main.route('/careers')
def careers():
    return render_template('company/careers.html')

@main.route('/privacy-policy')
def privacy_policy():
    return render_template('company/privacy_policy.html')

@main.route('/terms-of-service')
def terms_of_service():
    return render_template('company/terms_of_service.html')
