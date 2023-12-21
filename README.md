# Django RegistrationApp
- Two User Type Doctor or Patient can  Signup/Login in this app.

## Overview
- The Django Registration App is a web application built with Django that provides user registration functionality. It allows users to sign up for an account, log in, and view their details on profile Page.

## Features
- User Registration: Allow users to create an account by providing necessary information.
- User Authentication: Secure user authentication system for login and logout.
- Profile Dashboard: Users can see their profiles with additional information.
- Customizable: Easily customize and extend the RegistrationApp based on your project's needs.

## Requirements
- asgiref==3.7.2
- Django==5.0
- mysqlclient==2.2.0
- Pillow==10.1.0
- sqlparse==0.4.4
- tzdata==2023.3


## Installation

## Create and activate a virtual environment:
- python -m venv venv
- .\venv\Scripts\activate


## Clone the repository:
- git clone https://github.com/kksain/RegistrationApp.git

## Navigate to the project directory:
- cd RegistrationApp


## Install dependencies:
- pip install -r requirements.txt

## Apply migrations:
- python manage.py migrate

## Run the development server:
- python manage.py runserver

## Access the application at http://127.0.0.1:8000/.
