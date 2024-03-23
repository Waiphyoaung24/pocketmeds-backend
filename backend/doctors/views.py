# Create your views here.
from django.shortcuts import render
from db_connection import db
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from bson import json_util 
import json
from rest_framework import status
from bson.objectid import ObjectId



data = db["doc_info"]

class DoctorsListApiView(APIView):
  
  def get(self, request):
    currentList = list(data.find())
    if not currentList :
      return Response(
                {"res":"Data cannot be fetched"},
                status=status.HTTP_400_BAD_REQUEST
            )
    return Response(json.loads(json_util.dumps(currentList)),status=status.HTTP_200_OK)
  
class DoctorsDetailApiView(APIView):
  
  def get(self,request,doctors_id):
    objInstance = ObjectId(doctors_id)
    query = {'_id':objInstance}
    currentData = data.find_one(query)
    if not currentData :
      return Response(
                {"res": "Object with doctors id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
    return Response(json.loads(json_util.dumps(currentData)),status=status.HTTP_200_OK)