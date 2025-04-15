from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField(default='')
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,default=1)
    image = models.ImageField(upload_to='image/posts',blank=True,null=True)
    likes = models.IntegerField(null=True,blank=True,default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.CharField(max_length=70)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True) 
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='post_comments')
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return f"{self.author} on '{self.post}'"