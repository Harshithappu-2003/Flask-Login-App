# Flask Login App 🔐

## 📌 Description
This is a simple **Flask-based Login and Signup System** that allows users to register and log in. It includes:
- User authentication (Signup & Login)
- Basic form validation
- Flask template rendering

## 🚀 Features
✔️ User Registration (Signup)  
✔️ User Authentication (Login)  
✔️ Flask-based form handling  
✔️ Simple in-memory user database  

---

## 🛠️ Tech Stack
- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS (Jinja2 Templates)
- **Database:** Dictionary-based (can be replaced with SQLite/MySQL)
- **Environment Management:** `venv`
- **Package Manager:** `pip`

---

## 📁 Project Structure
Flask-Login-App/ │
── static/ # Static assets (CSS, JS) │
── templates/ # HTML templates │
── .env # Environment variables (optional) │
── app.py # Main Flask app │
── database.py # Handles user authentication logic │
── requirements.txt # Dependencies list │
── README.md # Project Documentation


---

## 📌 API Routes
# Route	Method	Description
/	GET	Redirects to /login
/login	GET/POST	Login Form
/signup	GET/POST	Signup Form
