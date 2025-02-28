from django.urls import path
from  .views import*

urlpatterns = [
    path('',base,name='base'),
    path('home/',home,name='home'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contacts'),
    path('booking/',booking,name='booking'),
    path('events/', events,name='events'),
    path('chat/', chat_view, name='chat'),

]

