from datetime import datetime

from django.db import models

# Create your models here.
from django.db import models

class django_site(models.Model):

    title  = models.CharField(max_length=20000)

class Article(models.Model):

    title       = models.CharField(max_length=20000)
    intro       = models.CharField(max_length=20000,default="")
    link        = models.CharField(max_length=1000)
    tag         = models.CharField(max_length=1000)
    source      = models.CharField(max_length=1000)
    date_pub    = models.DateTimeField(default=datetime.now, blank=True)
    date_save   = models.DateTimeField(default=datetime.now, blank=True)