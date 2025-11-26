from django.urls import path
from django_gist import views
urlpatterns = [
    path('getdata/<str:username>/', views.getData, name='getdata'),
    path('', views.getIndex, name='index')
]