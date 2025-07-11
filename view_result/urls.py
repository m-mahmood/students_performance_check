from django.urls import path
from . import views

urlpatterns = [
    path('', views.auth_login, name='login'),
    path('signup/', views.auth_signup, name='signup'),
    path('logout/', views.auth_logout, name='logout'),
    path('result/', views.get_result, name='result')
    
]
