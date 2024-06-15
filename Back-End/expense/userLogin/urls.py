from django.urls import path
from . import views
from .views import LogoutView

urlpatterns = [
    path("register", views.register_user, name="register_user"),
    path('home', views.Home.as_view()),
    path('logout/', LogoutView.as_view(), name='logout'),  # Add this line
]
