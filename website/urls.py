from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('contact', views.contact, name="contact"),
    path('blog', views.blog, name="blog"),
    path('about', views.about, name="about"),
    path('service', views.service, name="service"),
    path('portfolio', views.portfolio, name="portfolio"),
    path('single', views.single, name="single"),
    path('team', views.team, name="team"),
    path('appointment', views.appointment, name="appointment"),
]