from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView
# from .models import *
# Create your views here.
# index about booking contact team services testimonia tortyuztort
class Home(TemplateView):
    template_name = 'index.html'

class About(TemplateView):
    template_name = 'about.html'

class Contact(CreateView):
    # model = Contact
    template_name = 'contact.html'
    fields = "__all__"

class  Booking(ListView):
    template_name = 'booking.html'
class Team(TemplateView):
    template_name = 'team.html'

class Services(TemplateView):
    template_name = 'services.html'

class Testimonial(TemplateView):
    template_name = 'testimonial.html'

class tortyuztort(TemplateView):
    template_name = 'tortyuztort.html'
    

# def Team(request):
#     tem = Team.objects.all()
#     context = {
#         'team':tem
#     }
#     return render(request, 'team.html', context)



# def Service(request):
#     servis = Service.objects.all()
#     context = {
#         'servis':servis
#     }
#     return render(request,'services.html', context)


# def Testimonial(request):
#     Test = Testimonial.objects.all()
#     context = {
#         'Testimonial':Testimonial
#     }
#     return render(request,'testimonial.html', context)


# def Tortyuztort(request):
#     tort = Tortyuztort.objects.all()
#     context = {
#         'Tortyuztort':Tortyuztort
#     }
#     return render(request,'testimonia.html', context)