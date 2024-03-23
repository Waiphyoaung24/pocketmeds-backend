from django.shortcuts import render
from db_connection import db
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from bson import json_util 
import json
from rest_framework import status


class HealthConcernListApiView(APIView):

    def get(self,request):
        data = db["health_concerns_collection"]
        currentList = list(data.find())
        if not currentList:
            return Response(
                {"res":"Data cannot be fetch"},
                status=status.HTTP_400_BAD_REQUEST
            )
        return Response(json.loads(json_util.dumps(currentList)),status=status.HTTP_200_OK)

class LabTestWithHealthConcernIdApiView(APIView):
    def get(self,request,concern_id):
        data = db["lab_tests_collection"]
        query={'parent_id':concern_id}
        currentList = list(data.find(query))
        if not currentList :
         return Response(
                {"res": "Object with concern id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        return Response(json.loads(json_util.dumps(currentList)),status=status.HTTP_200_OK)