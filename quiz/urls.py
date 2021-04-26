from django.urls import path
from . import views

urlpatterns = [
    path('', views.display),
    path('submit', views.submit, name='submit_page')
]
