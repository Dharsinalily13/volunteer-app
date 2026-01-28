# Configuration file
import os

class Config:
    # Secret key for session & flash messages
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'my_super_secret_key'

    # MySQL Database settings
    MYSQL_HOST = 'localhost'      # Your DB host
    MYSQL_USER = 'root'           # Your MySQL username
    MYSQL_PASSWORD = 'your_password'  # Your MySQL password
    MYSQL_DB = 'helpize_db'       # Database name

    # Email settings (optional for contact notifications)
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'your_email@gmail.com'
    MAIL_PASSWORD = 'your_email_password'
