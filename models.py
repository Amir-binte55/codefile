from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


User=get_user_model()





class userProfile(models.Model):
    GENDER=(
        ("Male","Male"),
        ("Female", "Female"),
        ("Others", "Others"),
    )
    user= models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    gender=models.CharField(max_length=10 , choices=GENDER,null=True)
    image=models.ImageField(default='default.jpg',upload_to='profilePic',null=True)
    birthday=models.DateField(null=True)
    phone_number=models.IntegerField(null=True)
    address=models.TextField(max_length=200,null=True)

    def __str__ (self):
        return str(self.user)
