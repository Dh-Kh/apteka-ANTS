# Employee Management System

## Overview

This project is an Employee Management System built with Django, allowing users to register, login, create, view, update, and delete employee records. It also provides functionality for sorting, filtering, and displaying employee hierarchies.

## Table of Contents

- [Views](#views)
  - [Register](#register)
  - [Login](#login)
  - [Logout](#logout)
  - [Sort](#sort)
  - [Filter](#filter)
  - [Hierarchy](#hierarchy)
  - [Create](#create)
  - [Detail](#detail)
  - [Update](#update)
  - [Delete](#delete)

## Views

### Register

- **URL**: `/register/`
- **Description**: Allows users to register a new account.
- **Usage**: Open your browser and navigate to `/register/`. Fill out the registration form with the required information.

### Login

- **URL**: `/login/`
- **Description**: Provides a login form for users to access the system.
- **Usage**: Open your browser and navigate to `/login/`. Enter your login credentials to access the system.

### Logout

- **URL**: `/logout/`
- **Description**: Logs out the currently authenticated user and redirects to the login page.
- **Usage**: Click on the logout link in the application.

### Sort

- **URL**: `/sort/`
- **Description**: Displays a sorted list of employees based on the selected sorting option.
- **Usage**: Open your browser and navigate to `/sort/`. Use the sorting dropdown to select a sorting option.

### Filter

- **URL**: `/find/`
- **Description**: Allows users to filter employees by full name.
- **Usage**: Open your browser and navigate to `/find/`. Enter a full name in the search box to filter the employee list.

### Hierarchy

- **URL**: `/hierarchy/`
- **Description**: Displays the hierarchical tree of employees.
- **Usage**: Open your browser and navigate to `/hierarchy/`.

### Create

- **URL**: `/create/`
- **Description**: Allows authenticated users to create a new employee record.
- **Usage**: Open your browser and navigate to `/create/`. Fill out the employee creation form with the required information.

### Detail

- **URL**: `/employee/<int:pk>/`
- **Description**: Displays detailed information about a specific employee.
- **Usage**: Open your browser and navigate to `/employee/<employee_id>/`, replacing `<employee_id>` with the actual employee ID.

### Update

- **URL**: `/employee/<int:pk>/update/`
- **Description**: Allows authenticated users to update the information of a specific employee.
- **Usage**: Open your browser and navigate to `/employee/<employee_id>/update/`, replacing `<employee_id>` with the actual employee ID.

### Delete

- **URL**: `/employee/<int:pk>/delete/`
- **Description**: Allows authenticated users to delete a specific employee record.
- **Usage**: Open your browser and navigate to `/employee/<employee_id>/delete/`, replacing `<employee_id>` with the actual employee ID.

## Notes

- Make sure to replace `<employee_id>` with the actual ID of the employee you want to view, update, or delete.
- For views requiring authentication, ensure you are logged in before accessing them.
- manage.py seed_data Create 50000 records.
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py seed_data
python manage.py runserver

## Частина 1 (Обов'язкова)

### Відображення ієрархії

- Розроблено веб-сторінку для візуалізації ієрархії співробітників у вигляді деревоподібної структури.
- Інформація про співробітників зберігається в базі даних і включає ПІБ, посаду, дату прийому та електронну адресу.
- У кожного співробітника є один начальник.
- База даних містить не менше 50 000 співробітників, організованих на 7 рівнях ієрархій.
- Відображено посади співробітників у ієрархії.
- Створено базу даних за допомогою міграції Django.
- Реалізовано основний стиль за допомогою Twitter Bootstrap.

## Частина 2 (Опціональна)

### Заповнення бази даних

- Використано DB seeder Django ORM для заповнення бази даних початковими даними.

### Сторінка списку співробітників

- Реалізовано додаткову сторінку для відображення повного списку співробітників з усією доступною інформацією з бази даних.
- Забезпечено можливість сортування списку співробітників за будь-яким полем.

### Пошук співробітників

- Додано можливість виконувати пошук співробітників за будь-яким полем.

### Сортування та пошук AJAX

- Реалізовано AJAX для можливості сортування та пошуку без перезавантаження сторінки.

### Аутентифікація користувача

- Включено стандартні функції аутентифікації Django для захисту розділу веб-сайту, доступного тільки зареєстрованим користувачам.

### Операції CRUD

- Реалізовано операції CRUD (Створення, Читання, Оновлення, Видалення) для записів співробітників у розділі, доступному тільки для зареєстрованих користувачів.
- Всі поля, що стосуються користувачів, включаючи начальника кожного співробітника, є редагованими.

---

