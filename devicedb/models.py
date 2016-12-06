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

    def __str__(self):
        return self.model_name

class Notebook(models.Model):
    nb_id = models.CharField(max_length=200)
    model_name = models.CharField(max_length=200)
    cpu_core = models.CharField(max_length=200)
    cpu_speed = models.CharField(max_length=200)
    hdd_type = models.CharField(max_length=200)
    hdd_size = models.CharField(max_length=200)
    screen_size = models.CharField(max_length=200)
    price = models.CharField(max_length=200)

    def __str__(self):
        return self.model_name

class Smartphone(models.Model):
    sp_id = models.CharField(max_length=200)
    model_name = models.CharField(max_length=200)
    cpu_core = models.CharField(max_length=200)
    cpu_speed = models.CharField(max_length=200)
    flash_size = models.CharField(max_length=200)
    os = models.CharField(max_length=200)
    lte = models.CharField(max_length=200)
    price = models.CharField(max_length=200)

    def __str__(self):
        return self.model_name

class Product(models.Model):
    vendor = models.CharField(max_length=200)
    model_name = models.CharField(max_length=200)
    product_type = models.CharField(max_length=200)

    def __str__(self):
        return self.model_name