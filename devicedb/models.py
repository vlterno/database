from django.db import models
from django.utils import timezone


class Pc(models.Model):
    pc_id = models.CharField(max_length=200)
    model_name = models.CharField(max_length=200)
    cpu_core = models.CharField(max_length=200)
    cpu_speed = models.CharField(max_length=200)
    ram = models.CharField(max_length=200)
    hdd_size = models.CharField(max_length=200)
    price = models.CharField(max_length=200)

    # created_date = models.DateTimeField(
    #         default=timezone.now)
    # published_date = models.DateTimeField(
    #         blank=True, null=True)

    # def publish(self):
    #     self.published_date = timezone.now()
    #     self.save()

    # def __str__(self):
    #     return self.title