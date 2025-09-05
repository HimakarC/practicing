from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"), path('bring',views.bring, name="bring"), path('health/', health_check, name='health_check')
]
