from django.shortcuts import render
from django.http import HttpResponse

# view is a request handler or a function that takes a request and returns a response
def say_hello(request):
    return render(request, 'h.html', {'name': 'Brandon', 'age': 25})