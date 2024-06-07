#Importing the http
from django.http import HttpResponse

#defining the function to send the response as Hello, World!
def hello_world(request):
    return HttpResponse("Hello, World!")