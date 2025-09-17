# SwiftCart

SwiftCart is a Django-based e-commerce web application for browsing products, managing a shopping cart, and checking out.

## Tech Stack
- Django 5
- SQLite (default, can be swapped for PostgreSQL/MySQL)
- Bootstrap 5
- JavaScript (for cart interactions)


## Features

- User registration and login
- Product browsing and search
- Category and gender filters
- Add/remove products to/from cart
- Cart quantity management
- Checkout page

## Setup Instructions

1. **Clone the repository**
   ```sh
   git clone https://github.com/Shanitahisa/e-commcart
   cd e-commcart
   ```

2. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```

3. **Apply migrations**
   ```sh
   python manage.py migrate
   ```

4. **Create a superuser (optional)**
   ```sh
   python manage.py createsuperuser
   ```

5. **Run the development server**
   ```sh
   python manage.py runserver
   ```

6. **Access the app**
   Open [http://localhost:8000](http://localhost:8000) in your browser.

## Project Structure

- `swiftcart/` - Django project folder
- `swiftcarapp/` - Main app with models, views, templates
- `static/` - Static files (CSS, JS, images)
- `templates/` - HTML templates

## Notes

- Make sure your static and media files are correctly configured in `settings.py`.
- For image display, use `{% static %}` for static images and `{{ product.pImage.url }}` for uploaded images.

## License

MIT License
