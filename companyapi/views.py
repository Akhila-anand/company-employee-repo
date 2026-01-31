from django.http import HttpResponse

def home_page(request):
    print("home page requested")
    return HttpResponse("Welcome to the Company API Home Page")