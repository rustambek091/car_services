from django.urls import path 
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('about/', About.as_view(), name='about'),
    path('booking/', Booking.as_view(), name='booking'),
    path('contact/', Contact.as_view(), name='contact'),
    path('service/', Service(), name='service'),
    path('team/', Team(), name='team'),
    path('testimonial/', Testimonial(),name='testimonial'),
    path('tortyuztort/', Tortyuztort(), name='tortyuztort'),
]