# Import the Path class from pathlib to handle filesystem paths in a cross-platform way
from pathlib import Path

# Define the BASE_DIR as the parent directory of the current file
BASE_DIR = Path(__file__).resolve().parent.parent

# Define the SECRET_KEY used for cryptographic operations like signing cookies, etc.
SECRET_KEY = 'django-insecure-87fi8ad1ojjl1=-4al@*nystu65jblx$(*j=wot7+_d1f+wb1!'

# Set the DEBUG flag to True to enable debugging features
DEBUG = True

# List the allowed hostnames for this project. Using an empty list for now
ALLOWED_HOSTS = []

# List of installed applications
INSTALLED_APPS = [
    'django.contrib.admin', # Admin interface
    'django.contrib.auth',  # User authentication
    'django.contrib.contenttypes',  # Framework for content types
    'django.contrib.sessions',  # Session management
    'django.contrib.messages',  # Flash messaging framework
    'django.contrib.staticfiles',  # Management of static files like CSS and JS
    'app.apps.AppConfig',  # The custom app 'app'

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',  # Security middleware for handling security headers
    'django.contrib.sessions.middleware.SessionMiddleware', # Session management
    'django.middleware.common.CommonMiddleware',  # Common middleware for handling things like ETag and redirects
    'django.middleware.csrf.CsrfViewMiddleware', # CSRF protection middleware
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # User authentication middleware
    'django.contrib.messages.middleware.MessageMiddleware',  # Middleware for flashing messages
    'django.middleware.clickjacking.XFrameOptionsMiddleware', # Middleware for clickjacking protection
]

# The URL configuration for the project (main.urls model)
ROOT_URLCONF = 'main.urls'

# Template settings, specifying how Django should render HTML templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',  # Django template engine
        'DIRS': ['templates'],  # Look for templates in the 'templates' directory
        'APP_DIRS': True, # Enable template loading from app directories
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug', # Provides debug context for templates
                'django.template.context_processors.request', # Passes the request object to templates
                'django.contrib.auth.context_processors.auth',  # User authentication context
                'django.contrib.messages.context_processors.messages', # Message framework context
            ],
        },
    },
]

# WSGI application path for running the application in a WSGI server
WSGI_APPLICATION = 'main.wsgi.application'

# Database configuration, using SQLite by default and storing the database in the BASE_DIR
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Use SQLite database engine
        'NAME': BASE_DIR / 'db.sqlite3', # Database file path in the project root
    }
}

# Password validation settings, defining rules for strong passwords
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', # Similarity between user's attributes and password
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', # Minimum password length
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', # Prevent common passwords
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', # Prevent numeric-only passwords
    },
]

# Language settings for the application (set to 'en-us' for U.S. English)
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC' # Time zone settings (set to UTC by default)

# Internationalization settings (allowing for language and time zone support)
USE_I18N = True 
USE_TZ = True

# Static files URL settings (for serving CSS, JavaScript, images, etc.)
STATIC_URL = 'static/' 

# Default auto field for model primary keys (used to generate primary key fields automatically)
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
