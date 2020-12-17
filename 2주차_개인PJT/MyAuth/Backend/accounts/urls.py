from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('retrieve_password/', views.retrieve_password, name='retrieve_password'),
]