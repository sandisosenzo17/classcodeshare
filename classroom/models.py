from django.db import models
from django.contrib.auth import User

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


# Track the tasks created and submitted with their timestamps
class ActivityLog(models.Model):
  pass
