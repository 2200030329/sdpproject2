from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('module1.urls')),
    path('app/',include('crudapp.urls')),
    path('module2/',include('module2.urls')),
    path('mailapp/',include('mailapp.urls')),
    path('reviews/',include('reviews.urls')),
]
