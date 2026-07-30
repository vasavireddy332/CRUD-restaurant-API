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

```
crud-fastapi/
│
├── main.py             # FastAPI Application
├── database.py         # Database Configuration
├── models.py           # SQLAlchemy Models
├── schemas.py           # Pydantic Schemas
├── crud.py             # CRUD Operations
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/fastapi-ecommerce-api.git
cd fastapi-ecommerce-api
```

### 2️⃣ Create Virtual Environment

**Windows**

```bash
python -m venv crud
```

**Activate**

```bash
crud\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install fastapi
pip install uvicorn
pip install sqlalchemy
pip install pymysql
```

or

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Database

Create a MySQL database:

```sql
CREATE DATABASE restaurant_db;
```

Update the database connection inside `database.py`:

```python
DATABASE_URL = "mysql+pymysql://root:YOUR_PASSWORD@localhost:3306/restaurant_db"
```

> **Note:** If your MySQL password contains special characters such as `@`, encode them in the URL.
> Example: `@` → `%40`

### 5️⃣ Run the Application

```bash
uvicorn main:app --reload
```

Server starts at:

```
http://127.0.0.1:8000
```

---

## 📖 API Documentation

- **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 📌 Available Endpoints

| Method | Endpoint         | Description       |
|--------|------------------|--------------------|
| GET    | `/`              | Home Route         |
| GET    | `/products`      | Get All Products   |
| GET    | `/products/{id}` | Get Product by ID  |
| POST   | `/products`      | Create Product     |
| PUT    | `/products/{id}` | Update Product     |
| DELETE | `/products/{id}` | Delete Product     |

---

## 🗄️ Database

This project uses **MySQL** with **SQLAlchemy ORM**.

**Example Product Table**

| Field       | Type    |
|-------------|---------|
| id          | Integer |
| name        | String  |
| description | String  |
| price       | Float   |


---

## 💡 Learning Outcomes

Through this project, I learned:
- FastAPI fundamentals
- Building REST APIs
- SQLAlchemy ORM
- MySQL database connectivity
- CRUD operations
- API testing with Swagger
- Project structure and backend development

---

## 🔮 Future Improvements

- JWT Authentication
- User Login & Registration
- Role-Based Access Control
- Product Categories
- Search & Filtering
- Pagination
- Docker Support
- Deployment on Render/AWS

---

## 👩‍💻 Author

**Kadari Vasavi**
🎓 B.Tech Computer Science Student

🔗 [LinkedIn](https://www.linkedin.com/in/vasavi-kadari2006)

💻 Passionate about:
- Python
- FastAPI
- SQL
- Data Analytics
- Backend Development

---

⭐ **Support**

If you found this project helpful, consider giving it a star on GitHub!
