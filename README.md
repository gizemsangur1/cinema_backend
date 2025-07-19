# 🎬 Cinema Backend API

Cinema reservation system built with Django and Django REST Framework.

## ✅ Features

- User registration & JWT login system
- Movie management (list/create movies)
- Cinema halls with row/column seat structure
- Movie sessions (film + hall + datetime)
- Seat reservation with unique seat lock per session
- Dummy payment system (marks reservation as paid)

## 🏗 Tech Stack

- Python 3.x
- Django
- Django REST Framework
- Simple JWT

## 🚀 Setup

```
git clone https://github.com/yourusername/cinema_backend.git
cd cinema_backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
````

## 🔐 Auth
Use /api/users/register/ to register and /api/users/login/ to obtain JWT token.

Then include this in your headers:
````
Authorization: Bearer <your_access_token>
````

##📦 Endpoints
Users
POST /api/users/register/

POST /api/users/login/

POST /api/users/refresh/

Movies
GET /api/movies/

POST /api/movies/

Halls
GET /api/halls/

POST /api/halls/

Sessions
GET /api/bookings/sessions/

POST /api/bookings/sessions/

Reservations
POST /api/bookings/reserve/

Payments
POST /api/payments/pay/

## 🧪 Example Payment Payload
````
{
  "reservation": 5,
  "amount": "100.00"
}
````
