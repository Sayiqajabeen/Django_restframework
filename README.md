# Dispute Letter Generator

A Django REST API service that automatically generates dispute letters based on account and payment status criteria.

## 📋 Overview

This application provides an API endpoint that evaluates account data and generates appropriate dispute letters when specific conditions are met. The system determines eligibility for dispute letter generation based on payment status and account standing.

## 🔧 Features

- RESTful API for dispute letter processing
- PDF generation for dispute letters
- Conditional logic based on payment status and account standing
- Data validation and error handling
- Persistent storage of dispute requests

## 🛠️ Technology Stack

- **Backend**: Django 5.1.4
- **API**: Django REST Framework
- **Database**: SQLite (configurable)
- **PDF Generation**: ReportLab

## 🚀 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/dispute-letter-generator.git
   cd dispute-letter-generator
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

## 📝 API Usage

### Generate a Dispute Letter

**Endpoint**: `GET /api/process/`

**Query Parameters**:
- `payment_status`: Integer value representing payment status (e.g., 30, 60, 90)
- `account_status`: String value representing account status (e.g., 'paid', 'open')
- `creditor_remark`: String containing remarks from the creditor

**Example Request**:
```bash
curl "http://127.0.0.1:8000/api/process/?payment_status=30&account_status=open&creditor_remark=Account%20in%20dispute"
```

**Success Response**:
- If conditions are met: Returns a PDF document with the dispute letter
- If conditions are not met: Returns a JSON response explaining why a letter was not generated

**Error Response**:
- Status Code: 400 Bad Request
- Content: JSON object containing error details

## 💻 Development

### Project Structure

```
dispute_project/
├── api/                   # Main application directory
│   ├── migrations/        # Database migration files
│   ├── __init__.py
│   ├── admin.py           # Admin interface configuration
│   ├── apps.py            # Application configuration
│   ├── models.py          # Data models
│   ├── tests.py           # Test cases
│   ├── urls.py            # URL routing for the API
│   └── views.py           # View functions and business logic
├── dispute_project/       # Project settings directory
│   ├── __init__.py
│   ├── asgi.py            # ASGI configuration
│   ├── settings.py        # Project settings
│   ├── urls.py            # Project URL routing
│   └── wsgi.py            # WSGI configuration
├── manage.py              # Django management script
├── db.sqlite3             # SQLite database file
└── requirements.txt       # Project dependencies
```

### Business Logic

The application generates dispute letters when:
- Payment status is greater than or equal to 30 days
- Account status is either 'paid' or 'open'

## 🧪 Testing

Run the test suite with:
```bash
python manage.py test
```

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📬 Contact

Your Name - Sayiqa Jabeen

Project Link: [https://github.com/yourusername/dispute-letter-generator](https://github.com/yourusername/dispute-letter-generator)
