from django.apps import AppConfig

# References the AppConfig class defined above
class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'
