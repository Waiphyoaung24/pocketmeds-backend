from django.urls import path
from .views import MedicineListApiView
urlpatterns=[
    path('api', MedicineListApiView.as_view()),
]