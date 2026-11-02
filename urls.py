from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('doctors/', views.doctors_list, name='doctors_list'),
    path('blog-single/', views.blog_single, name='blog_single'),
    path('services/', views.services, name='services'),
    path('appointment/', views.appointment, name='appointment'),
    path('contact-submission/', views.contact_submission, name='contact'),
    path('appointment/', views.appointment, name='appointment'),
    path('about/', views.about, name='about'),
    path("newsletter/", views.newsletter_subscribe, name="newsletter"),

    
]