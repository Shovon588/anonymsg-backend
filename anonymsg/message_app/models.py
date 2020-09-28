from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime

# Create your models here.


class UserModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Message(UserModel):
    message = models.CharField(max_length=300)
    TYPE_CHOICE = (
    ('random', 'Random'),
    ('annonymouse', 'Anonymous')
    )
    type = models.CharField(max_length=64, choices=TYPE_CHOICE, blank=True, null=True)
    favorite = models.BooleanField(default=False)
    time = models.DateTimeField(default=timezone.now)

    def when(self):
        now = timezone.now()
        diff = now - self.time
        days = diff.days
        seconds = diff.seconds
        tot_minutes = seconds // 60
        tot_hours = tot_minutes // 60

        if days > 0:
            day = self.time.day
            month = self.time.month
            year = self.time.year
            hour = self.time.hour
            minute = self.time.minute
            print("in here")

            if hour > 12:
                meridiem = "PM"
                hour = hour-12
            else:
                meridiem = "AM"

            ret_obj = f"{day}-{month}-{year} {hour}:{minute} {meridiem}"
        else:
            try:
                minute = tot_minutes % (tot_hours*60)
            except ZeroDivisionError:
                minute = tot_minutes

            if tot_hours == 0:
                if minute == 1:
                    ret_obj = "1 minute ago"
                else:
                    ret_obj = f"{minute} minutes ago"
            else:
                if tot_hours == 1:
                    ret_obj = "1 hour ago"
                else:
                    ret_obj = f"{tot_hours} hours ago"

        return ret_obj

    def __str__(self):
        return self.message
