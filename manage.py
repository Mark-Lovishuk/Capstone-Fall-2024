# Import the os and sys modules for interacting with the operating system and handling command-line arguments
import os
import sys

# Define the main function that will run the Django management commands
def main():
    
    # Set the DJANGO_SETTINGS_MODULE environment variable to point to the project's settings module
    # Tells Django which settings to use when running commands
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')
      
    # Try to import the Django management command execution function
    try:
        from django.core.management import execute_from_command_line

        # If importing fails (Django is not installed or available), raise a custom error
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
      
    # Execute the command line arguments (this runs Django commands like 'runserver', 'migrate', etc.)
    execute_from_command_line(sys.argv)

# If this script is executed directly (not imported as a module), call the main function to run the management commands
if __name__ == '__main__':
    main()
