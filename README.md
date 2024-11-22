# E-Commerce Web Application

## Overview
This is a fully functional e-commerce web application that focuses on women’s clothing. It allows users to explore a catalog of products, add items to their shopping cart, and securely make purchases using Razorpay payment integration. The platform also features user account management and order tracking.

## Features
- **Product Catalog**: Display a wide variety of products with detailed descriptions.
- **User Authentication**: Register, log in, and manage user accounts.
- **Shopping Cart**: Add, remove, and update items in the shopping cart.
- **Order Management**: View order history and track purchases.
- **Payment Integration**: Secure payment processing using Razorpay.
- **Admin Panel**: Manage products, orders, and users via Django Admin.

## Technologies Used
- **Backend**: Python, Django, Django Rest Framework (DRF)
- **Frontend**: HTML, CSS, Bootstrap
- **Database**: MySql
- **Payment Gateway**: Razorpay
- **Version Control**: Git

## Installation and Setup
Follow the steps below to set up and run the project locally.

### Prerequisites
- Python 3.x installed
- Pip (Python package manager)
- Virtual environment (optional but recommended)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/Archanapola/Ecomm_project.git
Navigate to the project directory:
cd Ecomm_project

Create a virtual environment and activate it:
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

Install the required dependencies:
pip install -r requirements.txt

Run database migrations:
python manage.py makemigrations
python manage.py migrate

Create a superuser for admin access:
python manage.py createsuperuser

Start the development server:
python manage.py runserver

Usage
Open the application in your browser at http://127.0.0.1:8000/.
Log in or register to explore the store.
Admin access is available at http://127.0.0.1:8000/admin.
Project Structure
Ecomm_project/
├── accounts/                 # App handling user authentication and profiles
│   ├── __pycache__/          # Python cache files
│   ├── migrations/           # Database migration files
│   ├── static/               # Static files specific to the accounts app
│   ├── templates/            # Templates for accounts (HTML files)
│   ├── admin.py              # Admin configurations for the accounts app
│   ├── apps.py               # App configuration for accounts
│   ├── forms.py              # Form definitions for user input
│   ├── models.py             # Models for database schema
│   ├── tests.py              # Unit tests for the accounts app
│   └── views.py              # View logic for handling requests
|   |__ urls.py               # url configurations for the project 
├── ecomm/                    # Main project directory
│   ├── __pycache__/          # Python cache files
│   ├── __init__.py           # Project initialization file
│   ├── asgi.py               # ASGI configuration
│   ├── settings.py           # Django project settings
│   ├── urls.py               # URL configurations of the included apps
│   └── wsgi.py               # WSGI configuration
├── media/                    # Uploaded media files (images, documents, etc.)
├── static/                   # Global static files (CSS, JavaScript, images)
├── db.sqlite3                # SQLite database file
├── manage.py                 # Django project management script
├── myenv/                    # Virtual environment (optional, not part of the repo)

Future Enhancements
Add a wishlist feature for users.
Implement product recommendations based on user activity.

Contact
For any queries or suggestions, feel free to reach out to me:
Pola Archana
Email: archanapola.90@gmail.com
GitHub: Archanapola
