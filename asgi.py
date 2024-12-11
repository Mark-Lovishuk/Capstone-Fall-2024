import os

# This sets up the environment variable for Django's settings module
from django.core.asgi import get_asgi_application

# The settings module is where all configurations (like DATABASES, INSTALLED_APPS) are stored.
# Set to 'main.settings', meaning Django will look for a settings.py file in the 'main' directory.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')

# This gets the ASGI application, which is what the server will use to run Django asynchronously.
application = get_asgi_application()
