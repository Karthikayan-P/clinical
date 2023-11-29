from django.urls import path
from .views import CadminRegistrationView

urlpatterns = [
    path('register/',CadminRegistrationView.as_view(),name="register")
]