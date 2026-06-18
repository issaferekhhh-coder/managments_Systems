# 🧑‍💼 Employee Management System (Clean Architecture)

A Python-based Employee Management System built using **Clean Architecture principles**, including separation of layers, repository pattern, authentication system, and OOP design.

---

## 🚀 Features

- 👤 User Login System (Admin authentication)
- 🧑‍💼 Add, update, delete employees
- 📋 List all employees
- 🔐 Password hashing (SHA-256)
- 🏗️ Clean Architecture (Domain / Service / Infrastructure / UI)
- 🧩 Repository Pattern (decoupled data layer)
- 💾 In-memory database (easily extendable to SQLite/PostgreSQL)

---

## 🧠 Architecture

The project is divided into 4 main layers:

### 1. Domain Layer
- Core business models
- `Employee`, `User`

### 2. Application Layer
- Business logic
- `EmployeeService`, `AuthService`

### 3. Infrastructure Layer
- Data storage (InMemory repositories)
- `EmployeeRepository`, `UserRepository`

### 4. UI Layer
- Command Line Interface (CLI)
- User interaction and menu system

---

## 🔐 Login Credentials (Default)

Username: admin
Password: admin123
##########

---

## 🛠️ Technologies Used

- Python 3
- Dataclasses
- Abstract Base Classes (ABC)
- Hashlib (for password hashing)
- Type Hinting

---

 📂 Project Structure
 main.py:
 
*(Single-file version for simplicity. Can be split into modules later for production use.)*

---

 How to Run

 1. Clone the repository
```bash
git clone https://github.com/issaferekhhh-coder/managments_Systems.g

projects folder:
cd managments_Systems

run the program:
python main.py
###########
the  future is:
🔗 SQLite / PostgreSQL integration
🌐 REST API using FastAPI
🔑 JWT Authentication
🧪 Unit Testing (pytest)
🐳 Docker support
📊 Web Dashboard



Purpose of this Project:
This project is designed to demonstrate:
Real-world software architecture
Clean code principles
Backend system design
OOP and design patterns in Python



#######

👨‍💻 Author

Issa Ferekh

GitHub: https://github.com/issaferekhhh-coder

########3

If you like this project

Give it a star ⭐ and follow for more backend projects!
