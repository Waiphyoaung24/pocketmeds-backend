from django.urls import path
from .views import LabTestsListApiView,LabTestDetailApiView


urlpatterns =[
    path('api', LabTestsListApiView.as_view()),
    path('api/<labtest_id>/',LabTestDetailApiView.as_view())
]