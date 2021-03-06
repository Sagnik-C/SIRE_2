from django.db import models
import jsonfield
# Create your models here.
class filter(models.Model):
    username = models.CharField(max_length=20, unique=True, primary_key=True)
    qtype = models.CharField(max_length=50, default="all")
    ctype = models.CharField(max_length=50, default="all")
    vessel = models.TextField(default="all")
    hardrestype = models.CharField(max_length=50, default="all")
    humanrestype = models.CharField(max_length=50, default="all")
    procrestype = models.CharField(max_length=50, default="all")
    roviqlst = models.TextField(default="all")

    def __str__(self):
        return self.username

class gapAnalysis(models.Model):
        username = models.CharField(max_length=20, unique=True, primary_key=True)
        uid_json = jsonfield.JSONField()
        saved = models.CharField(max_length=50, default="no")

        def __str__(self):
             return self.username
