#!/usr/bin/env python3
"""
Create a simple default product image using PIL
"""

try:
    from PIL import Image, ImageDraw, ImageFont
    import os
    
    def create_default_image():
        # Create image
        img = Image.new('RGB', (300, 300), color='#BCA88D')
        
        # Create drawing context
        draw = ImageDraw.Draw(img)
        
        # Draw border
        draw.rectangle([10, 10, 290, 290], outline='#7D8D86', width=3, fill='#F1F0E4')
        
        # Draw icon (simple geometric shape)
        draw.ellipse([120, 80, 180, 140], outline='#7D8D86', width=3)
        draw.ellipse([140, 100, 160, 120], fill='#7D8D86')
        
        # Draw mountain/triangle shapes
        draw.polygon([(110, 180), (150, 140), (190, 180)], outline='#7D8D86', width=2)
        draw.polygon([(130, 180), (170, 150), (210, 180)], outline='#7D8D86', width=2)
        
        # Add text
        try:
            # Try to load a font
            font = ImageFont.truetype("arial.ttf", 16)
        except:
            # Use default font if Arial is not available
            font = ImageFont.load_default()
        
        # Draw text
        draw.text((150, 200), "Product Image", fill='#3E3F29', font=font, anchor='mm')
        draw.text((150, 220), "Not Available", fill='#7D8D86', font=font, anchor='mm')
        
        # Save image
        img_path = os.path.join('app', 'static', 'images', 'default-product.jpg')
        os.makedirs(os.path.dirname(img_path), exist_ok=True)
        img.save(img_path, 'JPEG', quality=85)
        print(f"Default product image created: {img_path}")
        return True
        
except ImportError:
    print("PIL/Pillow not available. Creating simple placeholder...")
    
    def create_default_image():
        # Create a simple HTML-based placeholder
        img_path = os.path.join('app', 'static', 'images', 'default-product.jpg')
        os.makedirs(os.path.dirname(img_path), exist_ok=True)
        
        # For now, we'll use the placeholder URLs in the application
        print("Using online placeholder images for default products")
        return True

if __name__ == '__main__':
    create_default_image()
