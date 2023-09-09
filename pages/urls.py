from django.urls import path 
from .views import *

urlpatterns = [
    path('', Home, name='home'),
    path('about/', About, name='about'),
    path('booking/', Booking, name='booking'),
    path('contact/', Contact, name='contact'),
    path('services/', Service, name='services'),
    path('team/', Team, name='team'),
    path('testimonial/', Testimonial,name='testimonial'),
    path('tortyuztort/', Tortyuztort, name='tortyuztort'),
]