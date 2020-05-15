from django.db import models

# Create your models here.
class GhostPost(models.Model):
    boast_or_roast = models.BooleanField(default=False)
    post = models.CharField(max_length=750)
    up_votes = models.IntegerField(default=0, blank=True, null=True)
    down_votes = models.IntegerField(default=0, blank=True, null=True)
    submission_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text 
