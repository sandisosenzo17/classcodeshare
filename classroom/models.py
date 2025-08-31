from django.db import models
from django.contrib.auth import get_user_model

# Retrieve the default User object
User = get_user_model()

# Details of the user and their role in the session
class UserProfile(models.Model):
  #These are the available roles a person can have
  ROLES = [
    ("host", "Host"),
    ("guest", "Guest")
  ]

  user = models.OneToOneField(User, on_delete=models.CASCADE)
  role = models.CharField(max_length=15, choices=ROLES)

  def __str__(self):
    return f"{self.user.username} - {self.role}"

# The session is created by the host at a geological location and time
class Session(models.Model):
  name = models.CharField(max_length=100)
  host = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="hosted_sessions")
  start = models.DateTimeField(auto_now_add=True)
  end = models.DateTimeField(null=True, blank=True)

  def __str__(self):
    return f"Session: {self.name}\nHost: {self.host}"


# The task assigned by the host to the audience
class Task(models.Model):
  title = models.CharField(max_length=150)
  description = models.TextField()
  session = models.ForeignKey(Session, on_delete=models.CASCADE, related_name="tasks")
  created_at = models.DateTimeField(auto_now_add=True)
  deadline = models.DateTimeField(null=True, blank=True)

  def __str__(self):
    return f"{self.created_at}\n{self.title} from session: {self.session.name}"


# This is a response from the guest to the host
class Submission(models.Model):
  task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="submissions")
  guest = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="submissions")
  code = models.TextField()
  code_result = models.TextField()
  time = models.DateTimeField(auto_now_add=True)
  geo_latitude = models.FloatField(null=True, blank=True)
  geo_longitude = models.FloatField(null=True, blank=True)
  late_submission = models.BooleanField(default=False)

  def __str__(self):
    return f"Task: {self.task.title} by {self.guest.user.username}"


# Track the tasks created and submitted with their timestamps
class ActivityLog(models.Model):
  Actions = [
    ("task_created", "Task Created"),
    ("task_submitted", "Task Submitted"),
    ("code_executed", "Code Executed")
  ]

  user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="activity_logs")
  action = models.CharField(max_length=30, choices=Actions)
  time = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return f"{self.user.username} did {self.action} at {self.time}"
