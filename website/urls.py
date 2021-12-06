from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('portfolio/', views.portfolio, name="portfolio"),
    path('pricing/', views.pricing, name="pricing"),
    path('services/', views.services, name="services"),
    path('booking/', views.booking, name="booking"),
    path('thank_you/', views.thank_you, name="thank_you"),
]
