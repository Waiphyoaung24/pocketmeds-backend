from django.shortcuts import render
from rest_framework.views import APIView
from db_connection import db
from rest_framework.response import Response
from django.http import HttpResponse
from bson import json_util 
import json
from rest_framework import status


class BookingLabTests(APIView):

    def get(self,request):
        data = db["booking_lab_tests"]
        currentList = list(data.find())
        if not currentList:
            return Response(
                {"res":"Data cannot be fetch"},
                status=status.HTTP_400_BAD_REQUEST
            )
        return Response(json.loads(json_util.dumps(currentList)),status=status.HTTP_200_OK)
    
    def post(self,request):
            database = db['booking_lab_tests']
            try:
                status = 200
                msg = "Data has been successfully inserted"
                data = request.data
                if data is None:
                    database.insert_one(data)
                else:
                     msg = "Data is empty"
            except Exception as e:
                status = 500
                msg = 'Server error, yo.'
    
            return Response({'message': msg},status = status)