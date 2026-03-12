# AI Student Management System

## Overview

The **AI Student Management System** is a web-based platform designed to digitize and automate common academic operations in educational institutions. Many colleges still rely on manual registers, spreadsheets, and disconnected tools to manage students, attendance, and assignments. This project aims to centralize these processes into a single system.

The platform allows administrators and teachers to manage students, classes, subjects, attendance, and assignments efficiently. Students are organized by **class groups (Department + Year)**, allowing teachers to distribute assignments and manage attendance for an entire class at once, similar to systems like Google Classroom.

The system is built using **Python and Django**, following modular architecture where each functional domain is separated into individual Django apps.

---

## Problem Statement

Educational institutions often face the following issues:

* Attendance maintained in paper registers
* Student records stored in scattered spreadsheets
* Difficulty tracking academic performance
* No centralized system for assignments and submissions
* Limited data analysis on student performance

These inefficiencies lead to data inconsistency, time loss, and poor monitoring of student progress.

---

## Solution

This project provides a **centralized digital platform** to manage academic workflows.

Key capabilities include:

* Student record management
* Class-based grouping of students
* Teacher and subject management
* Attendance tracking
* Assignment distribution to entire classes
* Performance tracking and future AI-based analytics

---

## System Architecture

Frontend
HTML, CSS, JavaScript

Backend
Django

Database
SQLite (development)

Future AI Module
Python Machine Learning models

---

## Project Structure

```
ai-student-management-system
│
├── backend
│   ├── academics
│   ├── students
│   ├── users
│   ├── attendance
│   └── college_ai
│
├── frontend
├── ai-module
├── docs
└── README.md
```

---

## Core Modules

### Users

Handles teacher management.

**Fields**

* Teacher ID
* Name
* Subject

---

### Students

Stores student information and links students to a class.

**Fields**

* Register Number
* Name
* Class

---

### Academics

Handles academic structure including classes and subjects.

**Class Structure**

```
Department + Year = Class
```

Example:

* IT Year 1
* IT Year 2
* CSE Year 1

---

### Attendance

Tracks attendance for students based on subject and date.

---

## Database Design

Relationship overview:

```
Class
  │
  ├── Students
  │
  ├── Assignments
  │
  └── Attendance
```

Teachers interact with **classes**, not individual students.

---

## Features

### Admin

* Manage classes
* Add subjects
* Manage teachers
* Monitor students

### Teacher

* View assigned classes
* Give assignments to entire class
* Track attendance

### Student

* View assignments
* Submit work
* Monitor academic records

---

## Technology Stack

Backend

* Python
* Django

Frontend

* HTML
* CSS
* JavaScript

Database

* SQLite

Libraries (planned)

* Pandas
* Scikit-learn

---

## Installation

Clone the repository

```
git clone https://github.com/yourusername/ai-student-management-system.git
```

Move to project folder

```
cd ai-student-management-system/backend
```

Create virtual environment

```
python -m venv venv
```

Activate environment

Windows

```
venv\Scripts\activate
```

Install dependencies

```
pip install django
```

Run migrations

```
python manage.py makemigrations
python manage.py migrate
```

Create superuser

```
python manage.py createsuperuser
```

Run the server

```
python manage.py runserver
```

Open admin panel

```
http://127.0.0.1:8000/admin
```

---

## Future Enhancements

* AI-based student performance prediction
* Risk detection for low-performing students
* Automated attendance analytics
* Student dashboard
* REST APIs using Django REST Framework
* Mobile application integration

---

## Learning Outcomes

This project demonstrates:

* Django modular architecture
* relational database design
* class-based academic grouping
* backend system development
* scalable project structure

---

## License

This project is created for educational and academic purposes.
