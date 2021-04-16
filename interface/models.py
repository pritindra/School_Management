from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Students(models.Model):
    # slug = models.OneToOneField(ItemObject,blank=True,null=True, on_delete=models.CASCADE)
    student_class = models.CharField(max_length=20)
    student_name = models.CharField(max_length=30, default='Gun')
    student_number = models.IntegerField()
    covid_checked = models.BooleanField()
    student_description = models.TextField(max_length=500,default='lorem ispum')
    covid_checked_2 = models.TextField(max_length=200)
    image = models.ImageField(default='default.jpg', upload_to='student_pics')

class Teachers(models.Model):
    # slug = models.OneToOneField(ItemObject,blank=True,null=True, on_delete=models.CASCADE)
    teacher_class = models.CharField(max_length=20)
    teacher_name = models.CharField(max_length=20, default='teacher')
    teacher_no = models.IntegerField()
    teacher_description = models.TextField(max_length=500,default='lorem ispum')
    covid_checked_2 = models.TextField(max_length=200)
    covid_checked = models.BooleanField()
    image = models.ImageField(default='default.jpg', upload_to='teachers_pics')

class Staffs(models.Model):
    staff_id = models.CharField(max_length=20)
    staff_name = models.CharField(max_length=20)
    job = models.CharField(max_length=30)
    job_desc = models.TextField(max_length=200,null=True, blank=True)
    staff_contact = models.TextField(max_length=200)
    covid_checked = models.BooleanField()
    covid_checked_2 = models.TextField(max_length=200)
    image = models.ImageField(default='job.jpg', upload_to='staff_pics')
