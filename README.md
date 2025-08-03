# 🏆 SpEquip - Sports Equipment E-Commerce Platform

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple.svg)](https://getbootstrap.com/)

A comprehensive sports equipment e-commerce web application built with modern web technologies. Features a complete shopping experience with user authentication, product management, shopping cart, wishlist, reviews, and admin dashboard.

![SpEquip Preview](https://via.placeholder.com/800x400/3E3F29/FFFFFF?text=SpEquip+E-Commerce+Platform)

## 🌟 Key Features

### 👤 **Customer Features**
- 🔐 **User Authentication** - Secure registration and login
- 🏪 **Product Catalog** - Browse sports equipment by categories
- 🔍 **Advanced Search** - Find products with search and filters
- 🛒 **Shopping Cart** - Add/remove items, quantity management
- ❤️ **Wishlist** - Save favorite items for later
- ⭐ **Reviews & Ratings** - Rate and review purchased products
- 📦 **Order Tracking** - View order history and status
- 💳 **Demo Checkout** - Simulated payment process

### 👨‍💼 **Admin Features**
- 📊 **Dashboard** - Sales analytics and store overview
- 📦 **Product Management** - CRUD operations for inventory
- 📋 **Order Management** - Update order statuses
- 👥 **User Management** - Monitor customer activity
- 📈 **Sales Analytics** - Track performance metrics

## 🎨 Design Theme
- **Primary**: #3E3F29 (Dark Olive)
- **Secondary**: #7D8D86 (Sage Green)
- **Accent**: #BCA88D (Beige)
- **Background**: #F1F0E4 (Light Cream)

## 🚀 Quick Start

### 📋 Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git

### ⚡ One-Click Setup

#### Windows
```cmd
# Clone the repository
git clone https://github.com/ivocreates/SportsEquip.git
cd SportsEquip

# Run automated setup
setup.bat
```

#### macOS/Linux
```bash
# Clone the repository
git clone https://github.com/ivocreates/SportsEquip.git
cd SportsEquip

# Make setup script executable and run
chmod +x setup.sh
./setup.sh
```

### 🔧 Manual Setup

1. **Clone Repository**
   ```bash
   git clone https://github.com/ivocreates/SportsEquip.git
   cd SportsEquip
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv venv
   
   # Activate virtual environment
   # Windows:
   venv\Scripts\activate
   
   # macOS/Linux:
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize Database**
   ```bash
   python setup.py
   python seed_database.py
   ```

5. **Run Application**
   ```bash
   python run.py
   ```

6. **Access Application**
   - Open browser and go to: `http://localhost:5000`

## 🔑 Demo Credentials

| Role | Email | Password |
|------|-------|----------|
| **Admin** | admin@spequip.com | admin123 |
| **Customer** | user@spequip.com | user123 |

## 🛠️ Tech Stack

### Frontend
- **HTML5** - Semantic markup structure
- **CSS3** - Modern styling with custom properties
- **JavaScript (ES6+)** - Interactive functionality
- **Bootstrap 5** - Responsive UI framework
- **Font Awesome** - Icons and visual elements

### Backend
- **Python 3.8+** - Core programming language
- **Flask 3.0** - Lightweight web framework
- **Flask-Login** - User session management
- **Flask-WTF** - Form handling and validation
- **SQLAlchemy** - ORM for database operations
- **Werkzeug** - Password hashing and utilities

### Database
- **SQLite** - Development database
- **Alembic** - Database migrations (ready for production)

### Development Tools
- **Git** - Version control
- **pip** - Python package manager
- **Virtual Environment** - Isolated dependencies

## 📁 Project Structure

```
📦 SpEquip/
├── 📁 app/                          # Main application package
│   ├── 📄 __init__.py              # Flask app factory
│   ├── 📄 models.py                # Database models
│   ├── 📄 routes.py                # Application routes
│   ├── 📄 forms.py                 # WTF Forms
│   ├── 📁 static/                  # Static assets
│   │   ├── 📁 css/
│   │   │   └── 📄 style.css        # Custom styles
│   │   ├── 📁 js/
│   │   │   └── 📄 main.js          # JavaScript functionality
│   │   └── 📁 images/
│   │       └── 📄 default-product.jpg
│   └── 📁 templates/               # Jinja2 templates
│       ├── 📄 base.html            # Base layout
│       ├── 📄 index.html           # Home page
│       ├── 📁 auth/                # Authentication pages
│       ├── 📁 products/            # Product pages
│       ├── 📁 cart/                # Shopping cart
│       ├── 📁 orders/              # Order management
│       ├── 📁 wishlist/            # Wishlist functionality
│       └── 📁 admin/               # Admin dashboard
├── 📁 instance/                     # Instance-specific files
├── 📄 requirements.txt              # Python dependencies
├── 📄 setup.py                     # Database setup
├── 📄 seed_database.py             # Sample data
├── 📄 run.py                       # Application entry point
├── 📄 setup.bat                    # Windows setup script
├── 📄 setup.sh                     # Unix/Linux setup script
├── 📄 test_deletion.py             # Test utilities
└── 📄 README.md                    # Project documentation
```

## 🔗 API Endpoints

### 🌐 Public Routes
| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Home page with featured products |
| `GET` | `/products` | Product catalog with filtering |
| `GET` | `/product/<id>` | Product details and reviews |
| `GET` | `/login` | User login page |
| `GET` | `/register` | User registration page |

### 🔒 User Routes (Authentication Required)
| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/add-to-cart` | Add item to shopping cart |
| `GET` | `/cart` | View shopping cart |
| `POST` | `/checkout` | Place order |
| `GET` | `/orders` | Order history |
| `GET` | `/wishlist` | User wishlist |
| `POST` | `/add-review` | Add product review |

### 👨‍💼 Admin Routes (Admin Access Required)
| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/admin` | Admin dashboard |
| `GET` | `/admin/products` | Product management |
| `POST` | `/admin/products/add` | Add new product |
| `PUT` | `/admin/products/<id>` | Update product |
| `DELETE` | `/admin/products/<id>` | Delete product |
| `GET` | `/admin/orders` | Order management |
| `PUT` | `/admin/orders/<id>` | Update order status |

## 🗄️ Database Schema

```sql
-- Users table
Users {
  id: INTEGER PRIMARY KEY
  username: VARCHAR(80) UNIQUE
  email: VARCHAR(120) UNIQUE
  password_hash: VARCHAR(200)
  is_admin: BOOLEAN
  created_at: DATETIME
}

-- Products table
Products {
  id: INTEGER PRIMARY KEY
  name: VARCHAR(100)
  description: TEXT
  price: FLOAT
  category: VARCHAR(50)
  image_url: VARCHAR(200)
  stock_quantity: INTEGER
  created_at: DATETIME
}

-- Orders table
Orders {
  id: INTEGER PRIMARY KEY
  user_id: INTEGER FK > Users.id
  total_amount: FLOAT
  status: VARCHAR(20)
  created_at: DATETIME
}

-- Order Items table
Order_Items {
  id: INTEGER PRIMARY KEY
  order_id: INTEGER FK > Orders.id
  product_id: INTEGER FK > Products.id
  quantity: INTEGER
  price: FLOAT
}

-- Cart Items table
Cart_Items {
  id: INTEGER PRIMARY KEY
  user_id: INTEGER FK > Users.id
  product_id: INTEGER FK > Products.id
  quantity: INTEGER
}

-- Reviews table
Reviews {
  id: INTEGER PRIMARY KEY
  user_id: INTEGER FK > Users.id
  product_id: INTEGER FK > Products.id
  rating: INTEGER (1-5)
  comment: TEXT
  created_at: DATETIME
}

-- Wishlist table
Wishlist {
  id: INTEGER PRIMARY KEY
  user_id: INTEGER FK > Users.id
  product_id: INTEGER FK > Products.id
  created_at: DATETIME
}
```

## ⚙️ Configuration & Customization

### 🎨 Changing Color Theme
Update CSS variables in `app/static/css/style.css`:
```css
:root {
    --primary-color: #your-color;
    --secondary-color: #your-color;
    --accent-color: #your-color;
    --background-color: #your-color;
}
```

### 📦 Adding New Product Categories
Edit the choices in `app/forms.py` in the `ProductForm` class:
```python
category = SelectField('Category', choices=[
    ('your_category', 'Your Category'),
    ('football', 'Football'),
    ('basketball', 'Basketball'),
    # ... existing categories
])
```

### 💳 Payment Integration
To integrate real payment processing:
1. Replace the demo checkout in `routes.py`
2. Add payment provider SDK (Stripe, PayPal, etc.)
3. Update checkout templates with payment forms
4. Add webhook handlers for payment events

### 🌍 Environment Variables
```bash
# Development
export FLASK_ENV=development
export SECRET_KEY=your-secret-key

# Production
export FLASK_ENV=production
export DATABASE_URL=your-database-url
export SECRET_KEY=your-production-secret
```

## 🚀 Development Guide

### 🔄 Running in Development Mode
```bash
# Activate virtual environment
source venv/bin/activate  # macOS/Linux
# or
venv\Scripts\activate     # Windows

# Set environment variables
export FLASK_ENV=development  # macOS/Linux
# or
set FLASK_ENV=development      # Windows

# Run with debug mode
python run.py
```

### 📝 Adding New Features
1. **Models**: Update `app/models.py` for database changes
2. **Routes**: Add endpoints in `app/routes.py`
3. **Templates**: Create/update HTML in `app/templates/`
4. **Styles**: Add CSS in `app/static/css/style.css`
5. **JavaScript**: Add functionality in `app/static/js/main.js`
6. **Forms**: Create forms in `app/forms.py`

### 🧪 Testing
```bash
# Run deletion tests
python test_deletion.py

# Add more tests as needed
python -m pytest tests/  # If using pytest
```

## 🐛 Troubleshooting

### Common Issues & Solutions

#### ❌ Import Errors
```bash
# Ensure virtual environment is activated
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# Install/reinstall dependencies
pip install -r requirements.txt
```

#### 🗄️ Database Errors
```bash
# Reset database completely
python -c "import os; os.remove('instance/spequip.db') if os.path.exists('instance/spequip.db') else None"

# Recreate database and data
python setup.py
python seed_database.py
```

#### 🔒 Permission Errors
```bash
# Unix/Linux: Make scripts executable
chmod +x setup.sh

# Windows: Run as administrator if needed
```

#### 🌐 Port Already in Use
```python
# Change port in run.py
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)  # Change port here
```

#### 💻 Flask-WTF Version Issues
```bash
# Install compatible version
pip install "Flask-WTF>=1.2.0"
```

### 🔄 Complete Reset
```bash
# Remove all generated files
rm -rf instance/ __pycache__/ app/__pycache__/  # Unix/Linux
# or
rmdir /s instance __pycache__ app\__pycache__   # Windows

# Reinstall and setup
pip install -r requirements.txt
python setup.py
python seed_database.py
```

## 🏭 Production Deployment

### 📋 Pre-deployment Checklist
- [ ] Change `SECRET_KEY` in production
- [ ] Set `FLASK_ENV=production`
- [ ] Use PostgreSQL/MySQL instead of SQLite
- [ ] Configure proper web server (Gunicorn/uWSGI)
- [ ] Set up reverse proxy (Nginx/Apache)
- [ ] Enable HTTPS/SSL certificates
- [ ] Configure environment variables
- [ ] Set up monitoring and logging

### 🔧 Production Configuration
```python
# app/__init__.py - Production settings
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'fallback-secret-key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///spequip.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
```

### 🌐 Web Server Setup (Gunicorn)
```bash
# Install Gunicorn
pip install gunicorn

# Run with Gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 run:app
```

### 🔒 Environment Variables
```bash
export SECRET_KEY="your-super-secret-production-key"
export DATABASE_URL="postgresql://user:password@localhost/spequip"
export FLASK_ENV="production"
```

## 🤝 Contributing

We welcome contributions to SpEquip! Here's how you can help:

### 🔀 Getting Started
1. **Fork** the repository
2. **Clone** your fork: `git clone https://github.com/your-username/SportsEquip.git`
3. **Create** a feature branch: `git checkout -b feature/amazing-feature`
4. **Make** your changes and test thoroughly
5. **Commit** your changes: `git commit -m "Add amazing feature"`
6. **Push** to your branch: `git push origin feature/amazing-feature`
7. **Open** a Pull Request

### 📝 Contribution Guidelines
- Follow PEP 8 style guidelines for Python code
- Add comments for complex logic
- Update documentation for new features
- Test your changes thoroughly
- Include type hints where applicable

### 🐛 Reporting Issues
- Use the GitHub issue tracker
- Include steps to reproduce the bug
- Provide system information (OS, Python version, etc.)
- Include error messages and logs

### 💡 Feature Requests
- Check existing issues first
- Clearly describe the feature and its benefits
- Consider implementation complexity

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2025 SpEquip

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

## 📞 Support & Contact

### 🆘 Need Help?
- 📖 **Documentation**: Check this README first
- 🐛 **Bug Reports**: [GitHub Issues](https://github.com/ivocreates/SportsEquip/issues)
- 💬 **Questions**: [GitHub Discussions](https://github.com/ivocreates/SportsEquip/discussions)
- 📧 **Email**: support@spequip.com

### 🌟 Show Your Support
If you find this project helpful, please consider:
- ⭐ Starring the repository
- 🍴 Forking and contributing
- 📢 Sharing with others
- 📝 Writing a review or blog post

## 🔮 Future Enhancements

### 🎯 Planned Features
- [ ] **Real Payment Gateway** - Stripe/PayPal integration
- [ ] **Email Notifications** - Order confirmations and updates
- [ ] **Advanced Search** - Elasticsearch integration
- [ ] **Product Recommendations** - ML-based suggestions
- [ ] **Mobile App** - React Native/Flutter app
- [ ] **Social Integration** - OAuth login, sharing
- [ ] **Multi-language Support** - i18n implementation
- [ ] **Advanced Analytics** - Detailed sales insights
- [ ] **Inventory Alerts** - Low stock notifications
- [ ] **Bulk Operations** - Import/export products
- [ ] **API Rate Limiting** - Enhanced security
- [ ] **Caching Layer** - Redis integration

### 🚀 Performance Improvements
- [ ] Database query optimization
- [ ] Image CDN integration
- [ ] Async task processing (Celery)
- [ ] Frontend caching strategies
- [ ] Progressive Web App (PWA) features

---

<div align="center">

**Made with ❤️ for the sports community**

[⬆ Back to Top](#-spequip---sports-equipment-e-commerce-platform)

</div>
