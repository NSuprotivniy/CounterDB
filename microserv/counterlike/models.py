import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
	pub_date = models.DateTimeField('date published')
	post_id=models.IntegerField(default=0)
	count_like=models.IntegerField(default=0)
	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
