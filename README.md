# 🛒 FastAPI E-Commerce CRUD API

A RESTful E-Commerce Backend API built using **FastAPI**, **SQLAlchemy**, and **MySQL**. This project demonstrates CRUD (Create, Read, Update, Delete) operations for managing products in an e-commerce system.

---

## 🚀 Features

- ✅ FastAPI REST API
- ✅ MySQL Database Integration
- ✅ SQLAlchemy ORM
- ✅ CRUD Operations
- ✅ Pydantic Validation
- ✅ Automatic API Documentation (Swagger UI)
- ✅ Clean Project Structure
- ✅ Virtual Environment Support

---

## 🛠️ Tech Stack

- Python 3.x
- FastAPI
- SQLAlchemy
- MySQL
- PyMySQL
- Pydantic
- Uvicorn

---

## 📂 Project Structure


crud-fastapi/
│
├── main.py # FastAPI Application
├── database.py # Database Configuration
├── models.py # SQLAlchemy Models
├── schemas.py # Pydantic Schemas
├── crud.py # CRUD Operations
├── requirements.txt
└── README.md


---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/fastapi-ecommerce-api.git
cd fastapi-ecommerce-api
#2️⃣ Create Virtual Environment

Windows

python -m venv crud

Activate

crud\Scripts\activate
# 3️⃣ Install Dependencies
pip install fastapi
pip install uvicorn
pip install sqlalchemy
pip install pymysql


Create a MySQL database

CREATE DATABASE restaurant_db;

Update the database connection inside database.py

DATABASE_URL = "mysql+pymysql://root:YOUR_PASSWORD@localhost:3306/restaurant_db"

Note: If your MySQL password contains special characters such as @, encode them in the URL.

# 5️⃣ Run the Application
uvicorn main:app --reload
Server starts at
http://127.0.0.1:8000
📖 API Documentation

http://127.0.0.1:8000/restautants
📌 Available Endpoints
Method	Endpoint	Description
GET	/	Home Route
GET	/products	Get All Products
GET	/products/{id}	Get Product by ID
POST	/products	Create Product
PUT	/products/{id}	Update Product
DELETE	/products/{id}	Delete Product
🗄️ Database

This project uses MySQL with SQLAlchemy ORM.

Example Product Table

Field	Type
id	Integer
name	String
description	String
price	Float

Swagger UI
MySQL Database
API Responses
VS Code Project Structure
💡 Learning Outcomes

Through this project, I learned:

FastAPI fundamentals
Building REST APIs
SQLAlchemy ORM
MySQL database connectivity
CRUD operations
API testing with Swagger
Project structure and backend development
🔮 Future Improvements
JWT Authentication
User Login & Registration
Role-Based Access Control
Product Categories
Search & Filtering
Pagination
Docker Support
Deployment on Render/AWS
👩‍💻 Author
Kadari Vasavi
🎓 B.Tech Computer Science Student
🔗 LinkedIn

[https://www.linkedin.com/in/vasavi-kadari](https://www.linkedin.com/in/vasavi-kadari)

💻 Passionate about

Python
FastAPI
SQL
Data Analytics
Backend Development
⭐ Support
If you found this project useful, please consider giving it a ⭐ on GitHub.
It motivates me to build and share more open-source projects!

If you found this project useful, please consider giving it a ⭐ on GitHub.

It motivates me to build and share more open-source projects!
