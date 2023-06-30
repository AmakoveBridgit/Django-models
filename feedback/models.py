from django.db import models

from django.db import models

class Feedback(models.Model):
    feedback_content=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    user_image=models.ImageField()
    ratings=models.CharField(max_length=5)
    feedback_status=models.CharField(max_length=20)
