from django.shortcuts import render, HttpResponse
from home.models import Contact
from datetime import datetime
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request, "home/index.html")

def about(request):
    return render(request, "home/about.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        detail = request.POST.get('detail')
        contact = Contact(name=name, email=email, detail=detail, date=datetime.today())
        contact.save()
        messages.success(request, "Your message has been send!")
    return render(request, "home/contact.html")

def privacy(request):
    return render(request, "home/privacy.html")

def terms(request):
    return render(request, "home/terms.html")

def gameplay(request):
    return render(request, "home/gameplay.html")

def tutorial(request):
    return render(request, "home/tutorial.html")