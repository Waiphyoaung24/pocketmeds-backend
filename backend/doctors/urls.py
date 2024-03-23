from django.urls import path
from .views import DoctorsDetailApiView,DoctorsListApiView


urlpatterns =[
    path('api/', DoctorsListApiView.as_view()),
    path('api/<doctors_id>/',DoctorsDetailApiView.as_view())
]