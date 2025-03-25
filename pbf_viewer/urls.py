from django.urls import  path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('load/', views.load_data, name='load_data'),
]

