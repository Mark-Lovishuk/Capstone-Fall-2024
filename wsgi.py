# Import the os module to interact with the operating system
import os

# Import the get_wsgi_application function from Django to create a WSGI application
from django.core.wsgi import get_wsgi_application

# Set the DJANGO_SETTINGS_MODULE environment variable to specify the settings module for Django
# Tells Django which settings to use for this project
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')

# Create the WSGI application callable that the web server will use to interact with Django
# This is the entry point for WSGI-compliant servers to communicate with the Django app
application = get_wsgi_application()
