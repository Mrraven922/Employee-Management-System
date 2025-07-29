# 🧑‍💼 Employee Management System

A simple desktop GUI application built using **Python (Tkinter)** and **SQLite3** to manage employee records including ID, Name, Age, Salary, and Department.

---

## 📌 Features

- ➕ Add new employees
- 🔄 Update employee information
- ❌ Delete employees
- 📄 View all records in a table
- 🧹 Clear form inputs
- ✅ Validates age and salary inputs
- 🗃️ SQLite-based backend

---

## 🖼️ Project Preview
<img width="1192" height="595" alt="output" src="https://github.com/user-attachments/assets/9a77df64-03f9-4e53-b256-0df500a671e8" />

---

## 🛠️ Tech Stack

| Layer       | Technology        |
|-------------|-------------------|
| Frontend    | Tkinter (Python GUI) |
| Backend     | SQLite3           |
| Validation  | Custom Python Functions |

---

## 🗂️ Project Structure

📁 Employee-Management-System/
│
├── main.py # Main GUI application

├── db_handler.py # Database logic (CRUD operations)

├── validation.py # Input validation functions

├── Employee.db # SQLite database file

├── output.png # Screenshot of the application

└── README.md # Project documentation


---

## 🚀 How to Run

1. 🐍 Make sure Python is installed.
2. 📁 Clone or download this repository.
3. 📦 Install required modules (if not already included):
   ```bash
   pip install tk

## ▶️ Run the app:

    python main.py

## ✔️ Validation Rules
 * Age: Must be a number between 18 and 65.

 * Salary: Must be a non-negative number.


