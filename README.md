# SpEquip - Sports Equipment E-Commerce Platform

A comprehensive sports equipment e-commerce web application built with HTML, CSS, JavaScript, Bootstrap, SQL, and Python Flask.

## Color Theme
- Primary: #3E3F29 (Dark Olive)
- Secondary: #7D8D86 (Sage Green)
- Accent: #BCA88D (Beige)
- Background: #F1F0E4 (Light Cream)

## Features

### User Features
- User registration and authentication
- Browse sports equipment by categories
- Product search and filtering
- Shopping cart functionality
- Wishlist management
- Product reviews and ratings
- Order placement and tracking
- Demo payment system
- Order history

### Admin Features
- Admin dashboard with analytics
- Product management (CRUD operations)
- Order management and status updates
- User management
- Inventory management
- Sales overview

## Tech Stack
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Backend**: Python Flask
- **Database**: SQLite (for development)
- **Authentication**: Flask-Login
- **Forms**: Flask-WTF
- **Password Hashing**: Werkzeug

## Project Structure
```
SpEquip/
├── app/
│   ├── __init__.py          # Flask app initialization
│   ├── models.py            # Database models
│   ├── routes.py            # Application routes
│   ├── forms.py             # WTF Forms
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css    # Custom styles
│   │   ├── js/
│   │   │   └── main.js      # JavaScript functionality
│   │   └── images/
│   │       └── default-product.jpg
│   └── templates/
│       ├── base.html        # Base template
│       ├── index.html       # Home page
│       ├── auth/            # Authentication templates
│       ├── products/        # Product templates
│       ├── cart/            # Shopping cart templates
│       ├── orders/          # Order templates
│       ├── wishlist/        # Wishlist templates
│       └── admin/           # Admin templates
├── instance/                # Instance folder for database
├── requirements.txt         # Python dependencies
├── setup.py                # Setup script
├── seed_database.py        # Database seeding script
├── run.py                  # Application runner
├── setup.bat               # Windows setup script
├── setup.sh                # Unix/Linux setup script
└── README.md               # This file
```

## Quick Setup (Automated)

### Windows
```bash
# Double-click setup.bat or run in Command Prompt:
setup.bat
```

### Unix/Linux/Mac
```bash
# Make executable and run:
chmod +x setup.sh
./setup.sh
```

## Manual Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation Steps

1. **Navigate to project directory**
   ```bash
   cd d:\freelance\SpEquip
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate virtual environment**
   ```bash
   # Windows
   venv\Scripts\activate
   
   # Unix/Linux/Mac
   source venv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Setup database and directories**
   ```bash
   python setup.py
   ```

6. **Seed database with sample data**
   ```bash
   python seed_database.py
   ```

7. **Run the application**
   ```bash
   python run.py
   ```

8. **Access the application**
   - Open browser: `http://localhost:5000`

## Default Login Credentials

### Admin Account
- **Email**: admin@spequip.com
- **Password**: admin123

### Demo User Account
- **Email**: user@spequip.com
- **Password**: user123

## Key Features Walkthrough

### For Users:
1. **Browse Products**: Navigate to Products page to see all available sports equipment
2. **Search & Filter**: Use search bar and category filters to find specific items
3. **Product Details**: Click on any product to see detailed information and reviews
4. **Shopping Cart**: Add items to cart and proceed to checkout
5. **Wishlist**: Save favorite items for later purchase
6. **Reviews**: Rate and review products you've purchased
7. **Order Tracking**: View order history and track current orders

### For Admins:
1. **Dashboard**: Overview of store statistics and recent orders
2. **Product Management**: Add, edit, or delete products from inventory
3. **Order Management**: View and update order statuses
4. **User Overview**: Monitor user registrations and activity

## API Endpoints

### Public Routes
- `GET /` - Home page
- `GET /products` - Product listing
- `GET /product/<id>` - Product details
- `GET /login` - Login page
- `GET /register` - Registration page

### User Routes (Login Required)
- `POST /add-to-cart` - Add item to cart
- `GET /cart` - Shopping cart
- `POST /checkout` - Place order
- `GET /orders` - Order history
- `GET /wishlist` - User wishlist
- `POST /add-review` - Add product review

### Admin Routes (Admin Access Required)
- `GET /admin` - Admin dashboard
- `GET /admin/products` - Product management
- `POST /admin/products/add` - Add new product
- `PUT /admin/products/<id>` - Update product
- `DELETE /admin/products/<id>` - Delete product
- `GET /admin/orders` - Order management
- `PUT /admin/orders/<id>` - Update order status

## Database Schema

### Users
- id, username, email, password_hash, is_admin, created_at

### Products
- id, name, description, price, category, image_url, stock_quantity, created_at

### Orders
- id, user_id, total_amount, status, created_at

### Order_Items
- id, order_id, product_id, quantity, price

### Cart_Items
- id, user_id, product_id, quantity

### Reviews
- id, user_id, product_id, rating, comment, created_at

### Wishlist
- id, user_id, product_id, created_at

## Customization

### Adding New Product Categories
Edit the choices in `app/forms.py` in the `ProductForm` class:
```python
category = SelectField('Category', choices=[
    ('your_category', 'Your Category'),
    # ... existing categories
])
```

### Changing Color Theme
Update CSS variables in `app/static/css/style.css`:
```css
:root {
    --primary-color: #your-color;
    --secondary-color: #your-color;
    --accent-color: #your-color;
    --background-color: #your-color;
}
```

### Payment Integration
To integrate real payment processing:
1. Replace the demo checkout in `routes.py`
2. Add payment provider SDK (Stripe, PayPal, etc.)
3. Update checkout templates with payment forms

## Development

### Running in Development Mode
```bash
# Activate virtual environment
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Set development environment
export FLASK_ENV=development  # or set FLASK_ENV=development on Windows

# Run with debug mode
python run.py
```

### Adding New Features
1. Update models in `app/models.py` if database changes are needed
2. Add routes in `app/routes.py`
3. Create/update templates in `app/templates/`
4. Add styling in `app/static/css/style.css`
5. Add JavaScript functionality in `app/static/js/main.js`

## Troubleshooting

### Common Issues

1. **Import Errors**
   - Ensure virtual environment is activated
   - Install requirements: `pip install -r requirements.txt`

2. **Database Errors**
   - Delete `instance/spequip.db` and run `python setup.py` again
   - Re-run `python seed_database.py`

3. **Permission Errors**
   - Ensure you have write permissions in the project directory
   - On Unix/Linux: `chmod +x setup.sh`

4. **Port Already in Use**
   - Change port in `run.py`: `app.run(debug=True, port=5001)`

### Reset Application
To completely reset the application:
```bash
# Remove database
rm instance/spequip.db

# Rerun setup
python setup.py
python seed_database.py
```

## Production Deployment

### Preparation for Production
1. Change secret key in `app/__init__.py`
2. Use PostgreSQL or MySQL instead of SQLite
3. Set `debug=False` in `run.py`
4. Configure proper web server (Gunicorn, uWSGI)
5. Set up reverse proxy (Nginx, Apache)
6. Configure environment variables for sensitive data

### Environment Variables for Production
```bash
export SECRET_KEY="your-secret-key"
export DATABASE_URL="your-database-url"
export FLASK_ENV="production"
```

## Contributing
1. Fork the repository
2. Create feature branch: `git checkout -b feature-name`
3. Make changes and test thoroughly
4. Commit changes: `git commit -m "Add feature"`
5. Push to branch: `git push origin feature-name`
6. Submit pull request

## License
This project is licensed under the MIT License.

## Support
For issues and questions:
- Check troubleshooting section above
- Create an issue in the repository
- Email: support@spequip.com

## Future Enhancements
- Real payment gateway integration
- Email notifications
- Advanced search with filters
- Product recommendations
- Mobile app
- Social media integration
- Multi-language support
- Advanced analytics dashboard
