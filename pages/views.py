from django.shortcuts import render
from .models import *
# Create your views here.

def Home(request):
    work = Work_time.objects.all()
    service = Our_services.objects.all()
    expert = Our_expert.objects.all()
    context = {
        'work': work,
        'service': service,
        'expert' : expert, 
    }
    return render(request, 'index.html', context)

def About(request):
    return render(request, 'about.html')


def Booking(request):
    return render(request, 'booking.html')
    
def Contact(request):
    contact = Contact.objects.all()
    context  = {
        'contact':contact,
    }
    return render(request, 'contact.html')

def Service(request):
    return render(request, 'service.html')

def Team(request):
    return render(request, 'team.html')

def Testimonial(request):
    return render(request, 'testimonial.html')

def Tortyuztort(request):
    return render(request, 'tortyuztort.html')

