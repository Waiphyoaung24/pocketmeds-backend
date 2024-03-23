from django.urls import path
from .views import index,VerifyOTPView


urlpatterns = [
    path('get',index),
    path('post',VerifyOTPView.as_view())
]