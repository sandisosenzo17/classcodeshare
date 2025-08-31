from django.contrib import admin
from .models import Session, UserProfile, Task, ActivityLog, Submission

admin.site.register(UserProfile)
admin.site.register(Session)
admin.site.register(Task)
admin.site.register(Submission)
admin.site.register(ActivityLog)