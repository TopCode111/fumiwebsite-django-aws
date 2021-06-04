from django.urls import path, include

from . import views

app_name = 'contact_form'

urlpatterns = [

    path('', views.home, name='index'),
    path('contact', views.contact, name='contact'),


]
