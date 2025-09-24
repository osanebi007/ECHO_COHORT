from django.urls import path
from users import views



urlpatterns = [
    path('register/', views.register),
    path('login/', views.login),
    path('author_onboarding/', views.create_author) 
]