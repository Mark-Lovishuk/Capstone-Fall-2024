# Import the render function from Django to render HTML templates
from django.shortcuts import render

# Define the view function for the 'index' page
# The 'request' parameter represents the HTTP request that triggered this view
def index(request):
    
    # Render the 'index.html' template and return the resulting HTTP response
    #Giving the template context
    return render(request, 'index.html')
