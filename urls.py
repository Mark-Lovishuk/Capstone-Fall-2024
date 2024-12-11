# Import the admin module from Django to register models with the admin site
from django.contrib import admin

# Import path and include functions to define URL patterns and include other URL configurations
from django.urls import path,include

# Define the URL patterns for the project
urlpatterns = [
    # Map the 'admin/' URL to the Django admin site
    # This allows access to the Django admin interface at '/admin/'
    path('admin/', admin.site.urls),
   
    # Include the URL patterns from the 'app.urls' module for the root URL ('')
    # This includes the app-specific URLs defined in 'app.urls'
    path('', include('app.urls')),
    
]
