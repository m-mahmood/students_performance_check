from django.urls import path
from . import views

urlpatterns = [
    path('result/', views.get_result, name='search-result'),
]
