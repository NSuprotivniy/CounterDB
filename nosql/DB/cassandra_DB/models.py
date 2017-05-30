from django.db import models
import uuid
from cassandra.cqlengine import columns
from django_cassandra_engine.models import DjangoCassandraModel

# Create your models here.
class LikeModel(DjangoCassandraModel):
    post_id = columns.Integer(primary_key = True)
    count_like = columns.Integer()
