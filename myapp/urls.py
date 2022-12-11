from django.urls import path
from . import views
from .forms import CustomLoginForm

app_name = 'app'

urlpatterns = [
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name='login')
]
