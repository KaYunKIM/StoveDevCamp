from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('retrieve_password/', views.retrieve_password, name='retrieve_password'),
]