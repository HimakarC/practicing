from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"), path('bring',views.bring, name="bring"), path('health/', health_check, name='health_check'), path('', views.my_view_1, name='service1_view'),
    path('', views.my_view_2, name='service2_view'),
]

