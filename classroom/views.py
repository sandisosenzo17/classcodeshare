from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import UserProfileSerializer, SessionSerializer, TaskSerializer, SubmissionSerializer, ActivityLogSerializer
from .models import UserProfile, Session, Submission, Task, ActivityLog
from django.http import JsonResponse
