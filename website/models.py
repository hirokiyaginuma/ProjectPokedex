from django.db import models
from django.db import models
from django.utils import timezone


class Main(models.Model):
    def __str__(self):
        return self.title