from django.db import models

# Create your models here.
class Teacher(models.Model):
    t_id = models.ImageField()
    t_name = models.CharField(max_length=40)
    t_email = models.EmailField(max_length=30)