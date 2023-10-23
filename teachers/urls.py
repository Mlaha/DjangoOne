from django.urls import path
from . import views

urlpatterns=[
    path('Home/',views.Home),
    path('About/',views.About),
    path('Services/',views.Services),
]
