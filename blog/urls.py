from django.urls import path
from . import views

urlpatterns = [
    
    path("single/<int:id>/", views.single, name="single"),
    path("category",views.category, name="category"),
    path('search/', views.search, name='search'),

]