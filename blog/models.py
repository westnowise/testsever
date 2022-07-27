from importlib.resources import contents
from turtle import Turtle
from django.db import models

# Create your models here.
class Post(models.Model):
    # id=models.AutoField(primary_key=True,null=False,blank=True)
    title = models.CharField(max_length=30)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'[{self.pk}] {self.title}'
    
    def get_absolute_url(self):
        return f'/{self.pk}/'

class Comment(models.Model):
    # id=models.AutoField(primary_key=True,null=False,blank=False)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    author=models.CharField(max_length=20)
    comment_text=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.author}::{self.comment_text}'
    
    def get_absolute_url(self):
        return f'{self.post.get_absolute_url()}#comment-{self.pk}'