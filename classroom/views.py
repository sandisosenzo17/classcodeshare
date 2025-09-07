from django.shortcuts import render
from .serializers import UserProfileSerializer, SessionSerializer, TaskSerializer, SubmissionSerializer, ActivityLogSerializer
from .models import UserProfile, Session, Submission, Task, ActivityLog
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def sessions(request):
  if request.method == 'GET':
    sessions = Session.objects.all()
    serializer = SessionSerializer(sessions, many=True)
    return JsonResponse({"sessions": serializer.data}, safe=False)
