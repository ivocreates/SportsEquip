// SpEquip E-Commerce Platform JavaScript

document.addEventListener('DOMContentLoaded', function() {
    // Initialize tooltips
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function(tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Initialize alerts with auto-dismiss
    initializeAlerts();
    
    // Initialize cart functionality
    initializeCart();
    
    // Initialize search functionality
    initializeSearch();
    
    // Initialize rating system
    initializeRating();
    
    // Initialize admin functionality
    initializeAdmin();
});

// Alert Management
function initializeAlerts() {
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        // Auto-dismiss alerts after 5 seconds
        setTimeout(() => {
            if (alert && alert.parentNode) {
                alert.style.opacity = '0';
                setTimeout(() => {
                    if (alert.parentNode) {
                        alert.remove();
                    }
                }, 300);
            }
        }, 5000);
        
        // Add close button functionality
        const closeBtn = alert.querySelector('.btn-close');
        if (closeBtn) {
            closeBtn.addEventListener('click', () => {
                alert.style.opacity = '0';
                setTimeout(() => alert.remove(), 300);
            });
        }
    });
}

// Cart Functionality
function initializeCart() {
    // Update cart quantity
    const quantityInputs = document.querySelectorAll('.quantity-input');
    quantityInputs.forEach(input => {
        input.addEventListener('change', function() {
            updateCartItemQuantity(this.dataset.cartId, this.value);
        });
    });
    
    // Add to cart buttons
    const addToCartBtns = document.querySelectorAll('.add-to-cart-btn');
    addToCartBtns.forEach(btn => {
        btn.addEventListener('click', function(e) {
            e.preventDefault();
            const productId = this.dataset.productId;
            const quantity = document.querySelector(`#quantity-${productId}`)?.value || 1;
            addToCart(productId, quantity);
        });
    });
    
    // Cart counter update
    updateCartCounter();
}

function addToCart(productId, quantity) {
    const formData = new FormData();
    formData.append('product_id', productId);
    formData.append('quantity', quantity);
    
    fetch('/add-to-cart', {
        method: 'POST',
        body: formData
    })
    .then(response => response.text())
    .then(data => {
        // Update cart counter
        updateCartCounter();
        // Show success message
        showAlert('Item added to cart!', 'success');
        // Small delay before reload to show the alert
        setTimeout(() => {
            window.location.reload();
        }, 1000);
    })
    .catch(error => {
        console.error('Error adding to cart:', error);
        showAlert('Error adding item to cart', 'danger');
    });
}

function updateCartItemQuantity(cartId, quantity) {
    const formData = new FormData();
    formData.append('cart_id', cartId);
    formData.append('quantity', quantity);
    
    fetch('/update-cart-quantity', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            updateCartDisplay();
        } else {
            showAlert('Error updating cart', 'danger');
        }
    })
    .catch(error => {
        console.error('Error updating cart:', error);
    });
}

function updateCartCounter() {
    // Fetch cart count from server
    fetch('/cart-count')
    .then(response => response.json())
    .then(data => {
        const counter = document.querySelector('.cart-counter');
        if (counter) {
            counter.textContent = data.count || 0;
        }
    })
    .catch(error => {
        console.error('Error fetching cart count:', error);
        // Fallback: count visible cart items
        const cartItems = document.querySelectorAll('.cart-item');
        const counter = document.querySelector('.cart-counter');
        if (counter) {
            counter.textContent = cartItems.length;
        }
    });
}

// Search Functionality
function initializeSearch() {
    const searchForm = document.querySelector('#search-form');
    const searchInput = document.querySelector('#search-input');
    const categoryFilters = document.querySelectorAll('.category-filter');
    
    if (searchForm) {
        searchForm.addEventListener('submit', function(e) {
            e.preventDefault();
            performSearch();
        });
    }
    
    if (searchInput) {
        // Debounced search
        let searchTimeout;
        searchInput.addEventListener('input', function() {
            clearTimeout(searchTimeout);
            searchTimeout = setTimeout(() => {
                if (this.value.length >= 3 || this.value.length === 0) {
                    performSearch();
                }
            }, 500);
        });
    }
    
    categoryFilters.forEach(filter => {
        filter.addEventListener('click', function(e) {
            e.preventDefault();
            filterByCategory(this.dataset.category);
        });
    });
}

function performSearch() {
    const searchTerm = document.querySelector('#search-input')?.value || '';
    const category = document.querySelector('.category-filter.active')?.dataset.category || '';
    
    const params = new URLSearchParams();
    if (searchTerm) params.append('search', searchTerm);
    if (category) params.append('category', category);
    
    window.location.href = `/products?${params.toString()}`;
}

function filterByCategory(category) {
    const params = new URLSearchParams(window.location.search);
    if (category) {
        params.set('category', category);
    } else {
        params.delete('category');
    }
    
    window.location.href = `/products?${params.toString()}`;
}

// Rating System
function initializeRating() {
    const ratingInputs = document.querySelectorAll('.rating-input');
    ratingInputs.forEach(input => {
        input.addEventListener('change', function() {
            updateStarDisplay(this);
        });
    });
    
    // Interactive star ratings
    const starRatings = document.querySelectorAll('.interactive-rating');
    starRatings.forEach(rating => {
        const stars = rating.querySelectorAll('.star');
        stars.forEach((star, index) => {
            star.addEventListener('click', () => {
                setRating(rating, index + 1);
            });
            
            star.addEventListener('mouseover', () => {
                highlightStars(rating, index + 1);
            });
        });
        
        rating.addEventListener('mouseleave', () => {
            const currentRating = rating.dataset.rating || 0;
            highlightStars(rating, currentRating);
        });
    });
}

function setRating(ratingElement, rating) {
    ratingElement.dataset.rating = rating;
    const hiddenInput = ratingElement.querySelector('input[type="hidden"]');
    if (hiddenInput) {
        hiddenInput.value = rating;
    }
    highlightStars(ratingElement, rating);
}

function highlightStars(ratingElement, rating) {
    const stars = ratingElement.querySelectorAll('.star');
    stars.forEach((star, index) => {
        if (index < rating) {
            star.classList.add('active');
        } else {
            star.classList.remove('active');
        }
    });
}

function updateStarDisplay(input) {
    const rating = input.value;
    const container = input.closest('.rating-container');
    if (container) {
        const stars = container.querySelectorAll('.star');
        stars.forEach((star, index) => {
            if (index < rating) {
                star.classList.add('filled');
            } else {
                star.classList.remove('filled');
            }
        });
    }
}

// Admin Functionality
function initializeAdmin() {
    // Confirm delete actions
    const deleteButtons = document.querySelectorAll('.delete-btn');
    deleteButtons.forEach(btn => {
        btn.addEventListener('click', function(e) {
            if (!confirm('Are you sure you want to delete this item?')) {
                e.preventDefault();
            }
        });
    });
    
    // Order status updates
    const statusSelects = document.querySelectorAll('.status-select');
    statusSelects.forEach(select => {
        select.addEventListener('change', function() {
            updateOrderStatus(this.dataset.orderId, this.value);
        });
    });
    
    // Live product preview
    const productForm = document.querySelector('#product-form');
    if (productForm) {
        const nameInput = productForm.querySelector('#name');
        const priceInput = productForm.querySelector('#price');
        const imageInput = productForm.querySelector('#image_url');
        
        if (nameInput) nameInput.addEventListener('input', updateProductPreview);
        if (priceInput) priceInput.addEventListener('input', updateProductPreview);
        if (imageInput) imageInput.addEventListener('input', updateProductPreview);
    }
}

function updateOrderStatus(orderId, status) {
    const formData = new FormData();
    formData.append('status', status);
    
    fetch(`/admin/orders/${orderId}/update-status`, {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            showAlert('Order status updated successfully', 'success');
            // Update status badge
            const statusBadge = document.querySelector(`#status-${orderId}`);
            if (statusBadge) {
                statusBadge.textContent = status;
                statusBadge.className = `badge status-${status}`;
            }
        } else {
            showAlert('Error updating order status', 'danger');
        }
    })
    .catch(error => {
        console.error('Error updating order status:', error);
        showAlert('Error updating order status', 'danger');
    });
}

function updateProductPreview() {
    const preview = document.querySelector('#product-preview');
    if (!preview) return;
    
    const name = document.querySelector('#name')?.value || 'Product Name';
    const price = document.querySelector('#price')?.value || '0.00';
    const imageUrl = document.querySelector('#image_url')?.value || '/static/images/default-product.jpg';
    
    preview.innerHTML = `
        <div class="card product-card">
            <img src="${imageUrl}" class="card-img-top" alt="${name}" onerror="this.src='/static/images/default-product.jpg'">
            <div class="card-body">
                <h5 class="card-title">${name}</h5>
                <p class="card-text price">₹${parseFloat(price).toFixed(2)}</p>
            </div>
        </div>
    `;
}

// Utility Functions
function showAlert(message, type = 'info') {
    const alertContainer = document.querySelector('#alert-container') || document.body;
    const alert = document.createElement('div');
    alert.className = `alert alert-${type} alert-dismissible fade show`;
    alert.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    
    alertContainer.insertBefore(alert, alertContainer.firstChild);
    
    // Auto-dismiss
    setTimeout(() => {
        alert.remove();
    }, 5000);
}

function formatCurrency(amount) {
    return new Intl.NumberFormat('en-US', {
        style: 'currency',
        currency: 'USD'
    }).format(amount);
}

function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Wishlist functionality
function addToWishlist(productId) {
    fetch(`/add-to-wishlist/${productId}`, {
        method: 'GET'
    })
    .then(response => response.text())
    .then(data => {
        showAlert('Item added to wishlist!', 'success');
        // Update wishlist button
        const btn = document.querySelector(`#wishlist-btn-${productId}`);
        if (btn) {
            btn.innerHTML = '<i class="fas fa-heart"></i> In Wishlist';
            btn.classList.remove('btn-outline-secondary');
            btn.classList.add('btn-secondary');
        }
    })
    .catch(error => {
        console.error('Error adding to wishlist:', error);
        showAlert('Error adding to wishlist', 'danger');
    });
}

// Image lazy loading
function initializeLazyLoading() {
    const images = document.querySelectorAll('img[data-src]');
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.classList.remove('lazy');
                imageObserver.unobserve(img);
            }
        });
    });
    
    images.forEach(img => imageObserver.observe(img));
}

// Initialize lazy loading when DOM is loaded
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initializeLazyLoading);
} else {
    initializeLazyLoading();
}
