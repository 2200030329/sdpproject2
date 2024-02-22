from django.contrib import admin
from django.urls import path
from .views import*

urlpatterns = [
    path('hello2/', hello1),
    path('hello/',hello, name= 'hello'),
    path('',newhomepage,name='newhomepage'),
    path('Travel/',Travel,name='TravelPackage'),
    path('print/',print_to_console,name='print_to_console'),
    path('p/',print1,name='print1'),
    path('places/',places,name='places'),
    path('ran1/',randomexample,name='randomexample'),
    path('randomotp/',randomotp,name='randomotp'),
    path('randomotp1/',randomotp1,name='randomotp1'),
    path('date/',getdate,name='getdate'),
    path('date1/',getdate1,name='getdate1'),
    path('tzfunctioncall/',tzfunctioncall,name='tzfunctioncall'),
    path('registercallfunction/',registercallfunction,name='registercallfunction'),
    path('registerloginfunction/',registerloginfunction,name='registerloginfunction'),
    path('pie_chart/',pie_chart,name='pie_chart'),
    path('signup',signup, name='signup'),
    path('signup1',signup1, name='signup1'),
    path('login',login, name='login'),
    path('login1',login1, name='login1'),
    path('logout',logout, name='logout'),
    path('contact',contact,name='contact'),
    path('contactmail',contactmail,name='contactmail'),

]

