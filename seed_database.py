#!/usr/bin/env python3
"""
SpEquip E-Commerce Platform Database Seeder
This script populates the database with sample data for testing and demonstration.
"""

import os
import sys
from datetime import datetime
import random

def seed_database():
    """Seed the database with sample data."""
    # Add current directory to Python path
    sys.path.insert(0, os.path.abspath('.'))
    
    try:
        from app import create_app, db
        from app.models import User, Product, Order, OrderItem, CartItem, Review, Wishlist
    except ImportError as e:
        print(f"Error importing modules: {e}")
        print("Please ensure the application is properly set up and dependencies are installed.")
        return False
    
    app = create_app()
    
    with app.app_context():
        print("Seeding database with sample data...")
        
        # Clear existing data
        print("Clearing existing data...")
        db.drop_all()
        db.create_all()
        
        # Create admin user
        admin = User(
            username='admin',
            email='admin@spequip.com',
            is_admin=True
        )
        admin.set_password('admin123')
        db.session.add(admin)
        
        # Create demo user
        demo_user = User(
            username='demo_user',
            email='user@spequip.com',
            is_admin=False
        )
        demo_user.set_password('user123')
        db.session.add(demo_user)
        
        # Create additional users
        users = []
        user_names = ['john_doe', 'jane_smith', 'mike_johnson', 'sarah_wilson', 'tom_brown']
        for i, username in enumerate(user_names):
            user = User(
                username=username,
                email=f'{username}@example.com',
                is_admin=False
            )
            user.set_password('password123')
            users.append(user)
            db.session.add(user)
        
        db.session.commit()
        print("Users created successfully!")
        
        # Create sample products
        products_data = [
            # Football
            {
                'name': 'Professional Football Helmet',
                'description': 'High-quality football helmet with advanced protection technology. Features impact-resistant shell and comfortable padding.',
                'price': 24899.17,  # ₹24,899 (converted from $299.99)
                'category': 'football',
                'image_url': 'https://via.placeholder.com/300x300/7D8D86/FFFFFF?text=Football+Helmet',
                'stock_quantity': 25
            },
            {
                'name': 'Football Shoulder Pads',
                'description': 'Lightweight yet durable shoulder pads designed for maximum protection and mobility on the field.',
                'price': 16599.17,  # ₹16,599 (converted from $199.99)
                'category': 'football',
                'image_url': 'https://via.placeholder.com/300x300/7D8D86/FFFFFF?text=Shoulder+Pads',
                'stock_quantity': 30
            },
            {
                'name': 'Official NFL Football',
                'description': 'Official size and weight football used in professional games. Perfect for practice and games.',
                'price': 4149.17,  # ₹4,149 (converted from $49.99)
                'category': 'football',
                'image_url': 'https://via.placeholder.com/300x300/7D8D86/FFFFFF?text=NFL+Football',
                'stock_quantity': 100
            },
            
            # Basketball
            {
                'name': 'Professional Basketball',
                'description': 'Official size basketball with superior grip and durability. Perfect for indoor and outdoor play.',
                'price': 3319.17,  # ₹3,319 (converted from $39.99)
                'category': 'basketball',
                'image_url': 'https://via.placeholder.com/300x300/BCA88D/FFFFFF?text=Basketball',
                'stock_quantity': 75
            },
            {
                'name': 'Basketball Hoop System',
                'description': 'Adjustable height basketball hoop system perfect for backyard play. Easy assembly included.',
                'price': 49799.17,  # ₹49,799 (converted from $599.99)
                'category': 'basketball',
                'image_url': 'https://via.placeholder.com/300x300/BCA88D/FFFFFF?text=Basketball+Hoop',
                'stock_quantity': 15
            },
            {
                'name': 'Basketball Shoes - Pro Series',
                'description': 'High-performance basketball shoes with excellent ankle support and traction for optimal court performance.',
                'price': 12449.17,  # ₹12,449 (converted from $149.99)
                'category': 'basketball',
                'image_url': 'https://via.placeholder.com/300x300/BCA88D/FFFFFF?text=Basketball+Shoes',
                'stock_quantity': 50
            },
            
            # Tennis
            {
                'name': 'Professional Tennis Racket',
                'description': 'Lightweight carbon fiber tennis racket with perfect balance for power and control.',
                'price': 16599.17,  # ₹16,599 (converted from $199.99)
                'category': 'tennis',
                'image_url': 'https://via.placeholder.com/300x300/3E3F29/FFFFFF?text=Tennis+Racket',
                'stock_quantity': 40
            },
            {
                'name': 'Tennis Ball Set (12 balls)',
                'description': 'Professional grade tennis balls with consistent bounce and durability. Perfect for practice and matches.',
                'price': 2074.17,  # ₹2,074 (converted from $24.99)
                'category': 'tennis',
                'image_url': 'https://via.placeholder.com/300x300/3E3F29/FFFFFF?text=Tennis+Balls',
                'stock_quantity': 80
            },
            {
                'name': 'Tennis Net - Tournament Grade',
                'description': 'Official tournament grade tennis net with adjustable height and weather-resistant materials.',
                'price': 7469.17,  # ₹7,469 (converted from $89.99)
                'category': 'tennis',
                'image_url': 'https://via.placeholder.com/300x300/3E3F29/FFFFFF?text=Tennis+Net',
                'stock_quantity': 20
            },
            
            # Soccer
            {
                'name': 'Professional Soccer Ball',
                'description': 'FIFA approved soccer ball with excellent flight characteristics and durability.',
                'price': 3817.17,  # ₹3,817 (converted from $45.99)
                'category': 'soccer',
                'image_url': 'https://via.placeholder.com/300x300/F1F0E4/000000?text=Soccer+Ball',
                'stock_quantity': 60
            },
            {
                'name': 'Soccer Goal Set',
                'description': 'Portable soccer goal set perfect for backyard practice. Easy setup and takedown.',
                'price': 10789.17,  # ₹10,789 (converted from $129.99)
                'category': 'soccer',
                'image_url': 'https://via.placeholder.com/300x300/F1F0E4/000000?text=Soccer+Goal',
                'stock_quantity': 25
            },
            {
                'name': 'Soccer Cleats - Elite',
                'description': 'Professional soccer cleats with superior traction and comfort for optimal field performance.',
                'price': 9959.17,  # ₹9,959 (converted from $119.99)
                'category': 'soccer',
                'image_url': 'https://via.placeholder.com/300x300/F1F0E4/000000?text=Soccer+Cleats',
                'stock_quantity': 45
            },
            
            # Fitness
            {
                'name': 'Adjustable Dumbbell Set',
                'description': 'Complete adjustable dumbbell set with multiple weight options. Perfect for home workouts.',
                'price': 33199.17,  # ₹33,199 (converted from $399.99)
                'category': 'fitness',
                'image_url': 'https://via.placeholder.com/300x300/7D8D86/FFFFFF?text=Dumbbells',
                'stock_quantity': 20
            },
            {
                'name': 'Yoga Mat - Premium',
                'description': 'Non-slip premium yoga mat with extra cushioning for comfort during workouts.',
                'price': 4149.17,  # ₹4,149 (converted from $49.99)
                'category': 'fitness',
                'image_url': 'https://via.placeholder.com/300x300/7D8D86/FFFFFF?text=Yoga+Mat',
                'stock_quantity': 100
            },
            {
                'name': 'Resistance Band Set',
                'description': 'Complete resistance band set with multiple resistance levels and accessories.',
                'price': 2489.17,  # ₹2,489 (converted from $29.99)
                'category': 'fitness',
                'image_url': 'https://via.placeholder.com/300x300/7D8D86/FFFFFF?text=Resistance+Bands',
                'stock_quantity': 75
            },
            
            # Running
            {
                'name': 'Running Shoes - Marathon',
                'description': 'Lightweight running shoes with excellent cushioning and support for long distance running.',
                'price': 10789.17,  # ₹10,789 (converted from $129.99)
                'category': 'running',
                'image_url': 'https://via.placeholder.com/300x300/BCA88D/FFFFFF?text=Running+Shoes',
                'stock_quantity': 60
            },
            {
                'name': 'Fitness Tracker Watch',
                'description': 'Advanced fitness tracker with heart rate monitoring, GPS, and smartphone connectivity.',
                'price': 16599.17,  # ₹16,599 (converted from $199.99)
                'category': 'running',
                'image_url': 'https://via.placeholder.com/300x300/BCA88D/FFFFFF?text=Fitness+Tracker',
                'stock_quantity': 35
            },
            
            # Swimming
            {
                'name': 'Swimming Goggles - Pro',
                'description': 'Anti-fog swimming goggles with UV protection and adjustable straps.',
                'price': 2074.17,  # ₹2,074 (converted from $24.99)
                'category': 'swimming',
                'image_url': 'https://via.placeholder.com/300x300/3E3F29/FFFFFF?text=Swimming+Goggles',
                'stock_quantity': 50
            },
            {
                'name': 'Swim Cap - Silicone',
                'description': 'Durable silicone swim cap that provides excellent water protection and comfort.',
                'price': 1078.17,  # ₹1,078 (converted from $12.99)
                'category': 'swimming',
                'image_url': 'https://via.placeholder.com/300x300/3E3F29/FFFFFF?text=Swim+Cap',
                'stock_quantity': 80
            },
            
            # Golf
            {
                'name': 'Golf Club Set - Beginner',
                'description': 'Complete golf club set perfect for beginners. Includes drivers, irons, wedges, and putter.',
                'price': 41499.17,  # ₹41,499 (converted from $499.99)
                'category': 'golf',
                'image_url': 'https://via.placeholder.com/300x300/F1F0E4/000000?text=Golf+Clubs',
                'stock_quantity': 15
            },
            {
                'name': 'Golf Balls - Tournament',
                'description': 'Professional grade golf balls with superior distance and control. Pack of 12.',
                'price': 2904.17,  # ₹2,904 (converted from $34.99)
                'category': 'golf',
                'image_url': 'https://via.placeholder.com/300x300/F1F0E4/000000?text=Golf+Balls',
                'stock_quantity': 100
            }
        ]
        
        products = []
        for product_data in products_data:
            product = Product(**product_data)
            products.append(product)
            db.session.add(product)
        
        db.session.commit()
        print(f"Created {len(products)} products successfully!")
        
        # Create sample reviews
        review_comments = [
            "Excellent quality product! Highly recommended.",
            "Great value for money. Works as expected.",
            "Good product but could be better.",
            "Amazing quality and fast shipping!",
            "Perfect for my needs. Will buy again.",
            "Decent product, nothing special.",
            "Outstanding quality and performance!",
            "Good but overpriced in my opinion.",
            "Exactly what I was looking for!",
            "Quality could be better for the price."
        ]
        
        # Add reviews for products
        for product in products[:10]:  # Review first 10 products
            num_reviews = random.randint(2, 5)
            for _ in range(num_reviews):
                user = random.choice(users)
                review = Review(
                    user_id=user.id,
                    product_id=product.id,
                    rating=random.randint(3, 5),
                    comment=random.choice(review_comments)
                )
                db.session.add(review)
        
        db.session.commit()
        print("Sample reviews created successfully!")
        
        # Create sample cart items for demo user
        cart_products = random.sample(products, 3)
        for product in cart_products:
            cart_item = CartItem(
                user_id=demo_user.id,
                product_id=product.id,
                quantity=random.randint(1, 3)
            )
            db.session.add(cart_item)
        
        db.session.commit()
        print("Sample cart items created successfully!")
        
        # Create sample wishlist items for demo user
        wishlist_products = random.sample(products, 5)
        for product in wishlist_products:
            wishlist_item = Wishlist(
                user_id=demo_user.id,
                product_id=product.id
            )
            db.session.add(wishlist_item)
        
        db.session.commit()
        print("Sample wishlist items created successfully!")
        
        # Create sample orders
        for user in users[:3]:  # Create orders for first 3 users
            num_orders = random.randint(1, 3)
            for _ in range(num_orders):
                order_products = random.sample(products, random.randint(1, 4))
                total_amount = 0
                
                order = Order(
                    user_id=user.id,
                    total_amount=0,  # Will calculate below
                    status=random.choice(['pending', 'confirmed', 'shipped', 'delivered'])
                )
                db.session.add(order)
                db.session.flush()  # Get order ID
                
                for product in order_products:
                    quantity = random.randint(1, 3)
                    order_item = OrderItem(
                        order_id=order.id,
                        product_id=product.id,
                        quantity=quantity,
                        price=product.price
                    )
                    total_amount += product.price * quantity
                    db.session.add(order_item)
                
                order.total_amount = total_amount
        
        db.session.commit()
        print("Sample orders created successfully!")
        
        print("\nDatabase seeding completed successfully!")
        print("\nSample Login Credentials:")
        print("Admin: admin@spequip.com / admin123")
        print("User:  user@spequip.com / user123")
        print("\nYou can now run 'python run.py' to start the application!")

if __name__ == '__main__':
    seed_database()
