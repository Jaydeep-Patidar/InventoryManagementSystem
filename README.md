# Inventory Management System Backend

A Django REST API backend for a comprehensive inventory management system, supporting both local development and production deployments with JWT authentication.

## Description

This backend provides a robust API for managing inventory operations, including categories, suppliers, customers, products, purchase orders, sales orders, stock transactions, and other related functions. It features secure JWT-based authentication, CORS support for frontend integration, and flexible database configurations for different environments.

## Features

- **JWT Authentication**: Secure token-based authentication with refresh tokens
- **Inventory Management**: Complete CRUD operations for all inventory entities
- **Stock Tracking**: Real-time stock levels, reorder alerts, and transaction history
- **Order Management**: Purchase and sales order processing
- **Multi-Environment Support**: Local (SQLite) and production (PostgreSQL) database configurations
- **CORS Enabled**: Ready for frontend integration
- **Admin Interface**: Django admin panel for data management
- **API Documentation**: RESTful endpoints with proper serialization

## Tech Stack

- **Backend**: Django 5.2.5, Django REST Framework
- **Authentication**: JWT (Simple JWT)
- **Database**: SQLite (local), PostgreSQL (production)
- **Deployment**: Gunicorn, WhiteNoise for static files
- **Environment Management**: python-decouple, django-environ
- **Other**: CORS headers, psycopg2-binary

## Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd inventory_fullstack/backend
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   Create a `.env` file in the root directory:
   ```env
   DJANGO_ENV=local
   DEBUG=True
   SECRET_KEY=your-secret-key-here
   ALLOWED_HOSTS=localhost,127.0.0.1
   CORS_ALLOWED_ORIGINS=http://localhost:5173,http://127.0.0.1:5173
   ```

   For production, set `DJANGO_ENV=production` and add database credentials:
   ```env
   DB_NAME=your-db-name
   DB_USER=your-db-user
   DB_PASSWORD=your-db-password
   DB_HOST=your-db-host
   DB_PORT=5432
   ```

## Setup

1. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

2. **Create a superuser (optional):**
   ```bash
   python manage.py createsuperuser
   ```
   Or use the temporary endpoint: `GET /create-admin/` (remove in production)

3. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

   The API will be available at `http://localhost:8000`

## API Endpoints

### Authentication
- `POST /api/accounts/auth/register/` - User registration
- `POST /api/accounts/auth/login/` - User login (returns access + refresh tokens)
- `POST /api/accounts/auth/refresh/` - Refresh access token
- `POST /api/accounts/auth/logout/` - Logout (blacklist refresh token)

### Inventory Management
- `GET/POST /api/categories/` - Category CRUD
- `GET/POST /api/suppliers/` - Supplier CRUD
- `GET/POST /api/customers/` - Customer CRUD
- `GET/POST /api/products/` - Product CRUD
- `GET /api/products/low_stock/` - Get products below reorder level
- `GET/POST /api/purchase-orders/` - Purchase order CRUD
- `GET/POST /api/sales-orders/` - Sales order CRUD

### Admin Interface
- Access Django admin at `/admin/` (requires superuser login)

## Usage

### Authentication Flow
1. Register a new user or login to get JWT tokens
2. Include the access token in the Authorization header for API requests:
   ```
   Authorization: Bearer <access_token>
   ```
3. Use the refresh token to get new access tokens when they expire

### Example API Usage
```bash
# Login
curl -X POST http://localhost:8000/api/accounts/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{"username": "your-username", "password": "your-password"}'

# Get products (requires auth)
curl -X GET http://localhost:8000/api/products/ \
  -H "Authorization: Bearer <access_token>"
```

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Make your changes and test thoroughly
4. Commit your changes: `git commit -am 'Add your feature'`
5. Push to the branch: `git push origin feature/your-feature`
6. Submit a pull request

## Support

For questions or issues, please open an issue on GitHub or contact [jaydeeppatidar2301@gmail.com].

