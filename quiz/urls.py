from django.urls import path
from . import views


urlpatterns = [
    path('viewquestions/', views.display),
    path('submit', views.submit, name='submit_page'),
    path('', views.allTweets, name='all'),
    path('', views.NewTweets, name='homepage'),

]
