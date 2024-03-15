from django.shortcuts import render
from db_connection import db
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from bson import json_util 
import json
from rest_framework import status
from bson.objectid import ObjectId



data = db["lab_tests_collection"]

class LabTestsListApiView(APIView):
  
  def get(self, request):
    currentList = list(data.find())
    if not currentList :
      return Response(
                {"res":"Data cannot be fetched"},
                status=status.HTTP_400_BAD_REQUEST
            )
    return Response(json.loads(json_util.dumps(currentList)),status=status.HTTP_200_OK)
  
class LabTestDetailApiView(APIView):
  
  def get(self,request,labtest_id):
    objInstance = ObjectId(labtest_id)
    query = {'_id':objInstance}
    currentData = data.find_one(query)
    if not currentData :
      return Response(
                {"res": "Object with labtest id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
    return Response(json.loads(json_util.dumps(currentData)),status=status.HTTP_200_OK)

  

  


