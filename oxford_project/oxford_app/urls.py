from django.urls import path,include
from oxford_app import views


urlpatterns = [
    path('', views.oxford, name='oxford')
]