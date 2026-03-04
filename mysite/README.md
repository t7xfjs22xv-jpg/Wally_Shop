# Simple Amazon-like Django Store

This workspace contains a minimal Django-based e-commerce store with:

- Product categories and listings
- Shopping cart for authenticated users
- Order creation
- Admin interface for managing products and orders
- Basic user authentication (login/logout)

## Setup Steps 🛠️

1. **Create virtual environment & install Django**
   ```bash
   python -m venv venv
   venv\Scripts\activate   # Windows
   pip install django
   ```
2. **Apply migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
3. **Create an admin user**
   ```bash
   python manage.py createsuperuser
   ```
4. **Populate some categories and products**
   - Visit `http://localhost:8000/admin` and log in.
   - Add `Category` and `Product` entries.

5. **Run development server**
   ```bash
   python manage.py runserver
   ```
   Access the site at `http://localhost:8000/`.

## Extending the Store

- Add product images with `ImageField` and configure `MEDIA_URL`/`MEDIA_ROOT`.
- Implement search, pagination, filtering.
- Integrate real payment gateways (Stripe, PayPal) at `order_create`.
- Add address/shipping models & checkout flow.
- Build templates with CSS/JS or migrate to a frontend framework.

> This scaffold gives you a starting point for a full Amazon‑like site. Customize and expand according to your needs!
