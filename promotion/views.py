from django.shortcuts import render

# Create your views here.
def index(request):
    
    context = {
               "example_attribute": "Hello, world",
               }
    
    return render(request, "promotion/index.html", context)