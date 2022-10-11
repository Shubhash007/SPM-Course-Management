from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import User_Role,Staff,Skill,Course,Registration,Job_Role,Requirements
from .serializers import StaffSerializer
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET', 'POST'])
@csrf_exempt
def staff_list(request):
    #get all staff
    if request.method == 'GET':
        staffs = Staff.objects.all()
        serializer = StaffSerializer(staffs, many=True)
        return Response({'staff': serializer.data},status = status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = StaffSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET', 'PUT', 'DELETE'])
@csrf_exempt
def staff_detail(request, query):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        staff = Staff.objects.get(Staff_ID=query)
    except Staff.DoesNotExist:
        return Response(data = "Cannot find user",status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StaffSerializer(staff)
        return Response(serializer.data, status = status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = StaffSerializer(staff, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        staff.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


