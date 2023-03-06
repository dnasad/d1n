from django.db import models

# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=50, blank=False)
    
    cost = models.IntegerField(default=0)


    def __str__(self):
        return self.name