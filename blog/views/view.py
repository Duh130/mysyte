from django.http import HttpResponse

def post_hello(request):
    return HttpResponse("Hello World")

def home(request):
    return HttpResponse("hello world")
