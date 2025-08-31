from rest_framework import serializers
from .models import UserProfile, Session, Task, Submission, ActivityLog

class UserProfileSerializer(serializers.ModelSerializer):
  class Meta:
    model = UserProfile
    fields = "__all__"

class SessionSerializer(serializers.ModelSerializer):
  # Allow showing details of the individual hosting the session
  host = UserProfileSerializer(read_only=True)

  class Meta:
    model = Session
    fields = "__all__"

class TaskSerializer(serializers.ModelSerializer):
  class Meta:
    model = Task
    fields = "__all__"


class SubmissionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Submission
    fields = "__all__"


class ActivityLogSerializer(serializers.ModelSerializer):
  class Meta:
    model = ActivityLog
    fields = "__all__"