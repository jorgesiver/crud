from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=140)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    picture = models.ImageField(upload_to='media/courses/pictures')

def __str__(self):
	return self.name