from django.urls import path
from .views import HealthConcernListApiView,LabTestWithHealthConcernIdApiView

urlpatterns = [
  path('api', HealthConcernListApiView.as_view()),
  path('api/<int:concern_id>/',LabTestWithHealthConcernIdApiView.as_view())
]