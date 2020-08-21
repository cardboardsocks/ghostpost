from django.db import models
from django.utils import timezone

# Create your models here.
class Roast_Boast(models.Model):
    is_boast = models.BooleanField(default=True)
    content = models.CharField(max_length=160)
    post_date = models.DateTimeField(default=timezone.now)
    upvote = models.IntegerField(default=0)
    downvote = models.IntegerField(default=0)
    @property
    def total(self):
        return (self.upvote - self.downvote)

