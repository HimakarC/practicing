from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('bring',views.bring, name="bring"),
    path('service1',views.home, name="home"),
    path('service2',views.home, name="home")
]



