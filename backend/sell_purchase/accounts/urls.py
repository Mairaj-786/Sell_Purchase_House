from django.urls import path
from .views import SignupView

urlpatterns = [
    path('singup', SignupView.as_view())
]
