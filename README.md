# Access the Application:

- The application is deployed on Streamlit, please note that it may have an initial startup time of up to 60 seconds as it's using a free service.
- URL: [Deployment URL](https://job-search-system-y10u.onrender.com)

# Job Search System Project Setup Guide

## Introduction
This guide will help you set up a Django project in your local environment. Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design.

## Prerequisites
- Python installed on your system (preferably Python 3.x)
- pip (Python package installer)
- Virtual environment (optional but recommended)

## Setup Instructions
1. **Clone the Repository:**
   ```bash
   git clone <repository-url>
   cd job_search_system
   
2. **Create Virtual Environment (Optional):**
   - For Windows:
     ```bash
     python -m venv venv
     ```
   - For MacOS/Linux:
     ```bash
     python3 -m venv venv
     ```

3. **Activate Virtual Environment:**
   - For Windows:
     ```bash
     venv\Scripts\activate
     ```
   - For MacOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install Django and Dependencies:**
   ```bash
   pip3 install -r requirements.txt

5. **Make Migrations and Migrate:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate

6.  **Create Superuser (Optional): (already created - admin, password)**
    
    - If you need an admin user for the Django admin panel, create one:
        
        ```bash
        
        `python manage.py createsuperuser`
        
7.  **Run the Development Server:**
    
    ```bash
    `python manage.py runserver`
    
8.  **Access the Application:**
    
    *   Open your web browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to see your Django application running.




