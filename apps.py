from django.apps import AppConfig

# this references the AppConfig class defined above
class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'
