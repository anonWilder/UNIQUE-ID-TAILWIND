from django.urls import path
from django.urls import path, include
from .views import UserRegistrationView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
]
path('', include('uniqueidgen.urls')),
