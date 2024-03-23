from django.urls import path
from .views import BookingLabTests


urlpatterns = [
    path('labtests',BookingLabTests.as_view())
]