from django.db import models

# Create your models here.
class Exam(models.Model):
    exam_name=models.CharField(max_length=101)
    exam_type=models.CharField(max_length=101)
    exam_time=models.CharField(max_length=101)
    exam_date=models.CharField(max_length=101)
    exam_marks=models.CharField(max_length=101)