from django.shortcuts import render
from .serializers import UserProfileSerializer, SessionSerializer, TaskSerializer, SubmissionSerializer, ActivityLogSerializer
from .models import UserProfile, Session, Submission, Task, ActivityLog
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def sessions(request):
  if request.method == 'GET':
    sessions = Session.objects.all()
    serializer = SessionSerializer(sessions, many=True)
    return JsonResponse({"sessions": serializer.data}, safe=False)
  elif request.method == 'POST':
    serializer = SessionSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)