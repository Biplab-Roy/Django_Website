from django.db import models

# Create your models here.

class Patient_Profile(models.Model):
    gender = [
        ('Male','Male'),
        ('Female','Female')    
    ]
    
    Patient_id = models.AutoField(primary_key=True)
    Patient_name = models.CharField(max_length = 20)
    Patient_avatar = models.ImageField(default='default.jpg', upload_to='profile_pics')
    Patient_mail = models.EmailField()
    Patient_age = models.IntegerField()
    Patient_gender = models.CharField(max_length = 10, choices = gender)
    Patient_password = models.CharField(max_length = 20)

    def __str__(self):
        return f"{self.Patient_name}"


