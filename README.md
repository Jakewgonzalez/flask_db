# Web Application Overview

This web application provides a secure platform for users to log in and access environmental sensor data. The application supports different user roles with varying levels of access and functionality.

## Features

### 1. User Authentication
- **Login**: Users can log in with a unique username and password.
- **Welcome Page**: Upon successful login, users are greeted with a welcome page.

### 2. Navigation Menu
The application features a simple navigation menu with the following options:

- **Home**: 
  - Displays the last login time.
  - Provides a brief description of each menu option.
  
- **View Environmental Results**: 
  - Shows temperature and relative humidity values from industrial control environmental sensors for the last 24 hours.
  
- **Logout**: 
  - Logs the user out and redirects back to the login screen.

## User Roles

### 1. User Role
- **Read Privileges**: Users with this role can view all web pages and data.

### 2. Administrator Role
- **Full Privileges**: Administrators have all user privileges plus the ability to:
  - **Insert**, **update**, and **delete** records in the sensor data files.
  - Manage these records through a dedicated web form.
