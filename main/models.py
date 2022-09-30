from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE,blank=True, )
    MATRIC_NO=models.CharField(blank=True, max_length=10)
    DEPARTMENT=models.CharField(blank=True,max_length=15)
    image=models.ImageField(blank=True, default='default.jpg', upload_to='profile_pic')

    def __str__(self):
        return f'{self.user.username} Profile'

class Result(models.Model):
     user=models.OneToOneField(User, on_delete=models.CASCADE)
     subject1=models.CharField(max_length=20)
     score1=models.CharField(max_length=3)
     subject2=models.CharField(max_length=20)
     score2=models.CharField(max_length=3)
     subject3=models.CharField(max_length=20)
     score3=models.CharField(max_length=3)
     subject4=models.CharField(max_length=20)
     score4=models.CharField(max_length=3)
     subject5=models.CharField(max_length=20)
     score5=models.CharField(max_length=3)
     subject6=models.CharField(max_length=20)
     score6=models.CharField(max_length=3)
     subject7=models.CharField(max_length=20)
     score7=models.CharField(max_length=3)
     subject8=models.CharField(max_length=20)
     score8=models.CharField(max_length=3)
     #Teacher_remark=models.TextField(max_length=300)
     def __str__(self):
        return f'{self.user.username} results'

