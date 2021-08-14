from django.shortcuts import render
from django.shortcuts import HttpResponse

def about (request):
    # return HttpResponse (" salam man shayan aiziz hastam!")
    return render (request, "about.html")
    
def home (request):
    # return HttpResponse ("this is main page!",)
    return render (request, "home.html")
    
