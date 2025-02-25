# Appointment Manager

The **Appointment Manager** is a modern and intuitive platform designed to simplify the management of appointments and patient follow-ups in healthcare facilities. Aimed at healthcare professionals, this system provides a smooth and efficient way to manage appointments, while offering powerful scheduling and tracking tools.

## Prerequisites

Before you begin, make sure you have the following installed on your machine:

- Python 3.12
- Django 5.1.4
- Docker 28.0.0

## Installation and Setup

### 1. Create a project folder
In your terminal, create a folder to store the project:


## bash
mkdir appoint


### 2. Create and activate a virtual environment
- cd appoint
- python -m venv my_env
- source my_env/bin/activate (linux)
- my_env\Scripts\activate (windows)

### 3. Clone the GitHub repository
- git clone https://github.com/Thierdl/Gestionnaire-de-Rendez-Vous.git


### 4. Install dependencies
- cd Gestionnaire-de-Rendez-Vous
- pip install -r requirements.txt
- pip freeze > requirements.txt

## Running the Project
### 1. Build the Docker image
- docker build -t project .

### 2. Start the Django server
- python3 manage.py runserver

The server will be accessible at http://localhost:8000 or http://127.0.0.1:8000.
