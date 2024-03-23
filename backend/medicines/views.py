from django.shortcuts import render
from django.http import HttpResponse
from db_connection import db
from rest_framework.views import APIView
from rest_framework.response import Response
from bson import json_util 
import json
from rest_framework import status
from bson.objectid import ObjectId

data = db['medicine_collection']


class MedicineListApiView(APIView):
    def get(self,request):
        currentList = list(data.find())
        if not currentList:
            return Response({"res": "Data cannot be fetched"},
                            status = status.HTTP_400_BAD_REQUEST)
        return Response(json.loads(json_util.dumps(currentList)))
