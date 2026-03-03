# Personal Finance Tracker (Prototype Phase)

## Project Overview

This project is a web-based Personal Finance Tracker developed using Django and SQLite. 

The prototype phase includes:

- User Registration
- User Login / Logout
- Add Expense
- View Expenses
- Category-wise Expense Visualization (Matplotlib Pie Chart)

This prototype demonstrates core backend functionality, database integration, and data visualization.

---

## Technology Stack

Backend Framework: Django  
Database: SQLite  
Visualization: Matplotlib  
Language: Python  
Frontend: HTML  

---

## How to Download from GitHub

1. Open the repository link.
2. Click on the green "Code" button.
3. Select "Download ZIP".
4. Extract the ZIP file.

OR clone using Git: git clone <https://github.com/fahadali87/finance_tracker.git>


---

## Installation Guide

### Step 1: Install Python

Download and install Python from:
https://www.python.org/downloads/

While installing:
✔ Check "Add Python to PATH"

Verify installation: python --version

---

### Step 2: Create Virtual Environment

Navigate to project folder: cd finance_tracker

Create virtual environment: python -m venv venv

Activate virtual environment: venv\Scripts\activate

Windows:
---

### Step 3: Install Dependencies

Install required packages: pip install -r requirements.txt

---

### Step 4: Apply Migrations : python manage.py migrate

---

### Step 5: Create Superuser (Optional - For Admin Access) : python manage.py createsuperuser

---

### Step 6: Run Development Server : python manage.py runserver

Open browser and visit: http://127.0.0.1:8000

---

## Features Implemented

- Secure User Authentication
- Expense Model with User Relationship
- Expense Entry Form
- Expense Listing Table
- Category-wise Expense Chart (Matplotlib)
- SQLite Database Integration

---

## Notes

- This is a prototype phase submission.
- Advanced features like income tracking, editing, deletion, prediction, export, and backup will be implemented in future phases.
