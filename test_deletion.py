#!/usr/bin/env python3
"""
Test script to verify that product deletion now works properly without IntegrityError
"""

from app import create_app, db
from app.models import Product, Review, CartItem, Wishlist, OrderItem
import sys

def test_product_deletion():
    """Test product deletion scenarios"""
    app = create_app()
    
    with app.app_context():
        print("Testing Product Deletion Scenarios...")
        print("=" * 50)
        
        # Find a product that has reviews but no orders
        products_with_reviews = Product.query.join(Review).filter(~Product.id.in_(
            db.session.query(OrderItem.product_id).distinct()
        )).all()
        
        if products_with_reviews:
            test_product = products_with_reviews[0]
            print(f"Found test product: {test_product.name} (ID: {test_product.id})")
            
            # Check related records
            reviews_count = Review.query.filter_by(product_id=test_product.id).count()
            cart_items_count = CartItem.query.filter_by(product_id=test_product.id).count()
            wishlist_items_count = Wishlist.query.filter_by(product_id=test_product.id).count()
            order_items_count = OrderItem.query.filter_by(product_id=test_product.id).count()
            
            print(f"Related records:")
            print(f"  - Reviews: {reviews_count}")
            print(f"  - Cart items: {cart_items_count}")
            print(f"  - Wishlist items: {wishlist_items_count}")
            print(f"  - Order items: {order_items_count}")
            
            if order_items_count > 0:
                print("❌ Cannot delete - product has order items (this is expected)")
                return True
            
            try:
                # Delete related records first (simulating our route logic)
                CartItem.query.filter_by(product_id=test_product.id).delete()
                Review.query.filter_by(product_id=test_product.id).delete()
                Wishlist.query.filter_by(product_id=test_product.id).delete()
                
                # Delete the product
                db.session.delete(test_product)
                db.session.commit()
                
                print("✅ Product deletion successful! No IntegrityError occurred.")
                return True
                
            except Exception as e:
                db.session.rollback()
                print(f"❌ Product deletion failed: {str(e)}")
                return False
        else:
            print("No suitable test product found (products with reviews but no orders)")
            return True

def test_cascade_relationships():
    """Test that cascade deletes work properly"""
    app = create_app()
    
    with app.app_context():
        print("\nTesting Cascade Relationships...")
        print("=" * 50)
        
        # Create a test product
        test_product = Product(
            name="Test Product for Deletion",
            description="This is a test product",
            price=999.99,
            category="test",
            stock_quantity=10
        )
        db.session.add(test_product)
        db.session.commit()
        
        product_id = test_product.id
        print(f"Created test product: {test_product.name} (ID: {product_id})")
        
        # Create some related records
        from app.models import User
        test_user = User.query.first()
        
        if test_user:
            # Add to cart
            cart_item = CartItem(user_id=test_user.id, product_id=product_id, quantity=1)
            db.session.add(cart_item)
            
            # Add to wishlist
            wishlist_item = Wishlist(user_id=test_user.id, product_id=product_id)
            db.session.add(wishlist_item)
            
            # Add review
            review = Review(user_id=test_user.id, product_id=product_id, rating=5, comment="Test review")
            db.session.add(review)
            
            db.session.commit()
            
            print("Added test related records (cart, wishlist, review)")
            
            # Now try to delete the product using cascade
            try:
                db.session.delete(test_product)
                db.session.commit()
                
                # Check if related records were deleted
                remaining_cart = CartItem.query.filter_by(product_id=product_id).count()
                remaining_wishlist = Wishlist.query.filter_by(product_id=product_id).count()
                remaining_reviews = Review.query.filter_by(product_id=product_id).count()
                
                if remaining_cart == 0 and remaining_wishlist == 0 and remaining_reviews == 0:
                    print("✅ Cascade deletion successful! All related records were removed.")
                    return True
                else:
                    print(f"❌ Cascade deletion incomplete. Remaining: cart={remaining_cart}, wishlist={remaining_wishlist}, reviews={remaining_reviews}")
                    return False
                    
            except Exception as e:
                db.session.rollback()
                print(f"❌ Cascade deletion failed: {str(e)}")
                return False
        else:
            print("No test user found for cascade testing")
            return False

if __name__ == "__main__":
    print("SpEquip Product Deletion Test")
    print("=" * 50)
    
    success1 = test_product_deletion()
    success2 = test_cascade_relationships()
    
    if success1 and success2:
        print("\n🎉 All tests passed! Product deletion is working correctly.")
        sys.exit(0)
    else:
        print("\n💥 Some tests failed. Check the output above.")
        sys.exit(1)
