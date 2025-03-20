from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='home'),
    path('chatbot', chatbot_view, name='chatbot'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),

]