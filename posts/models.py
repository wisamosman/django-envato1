from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Post(models.Model):
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to='post')
    description = models.TextField(max_length=30000)
    likes = models.ManyToManyField(User, related_name='post_like')
    
    def __str__(self):
        return self.name
    



class Review(models.Model):
    user = models.ForeignKey(User,related_name='user_review',on_delete=models.SET_NULL,null=True,blank=True)
    post = models.ForeignKey(Post,related_name='post_review',on_delete=models.SET_NULL,null=True,blank=True)
    review = models.TextField(max_length=500)
    rate = models.IntegerField(validators=[MaxValueValidator(50),MinValueValidator(0)])
    create_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.user} = {self.post}"