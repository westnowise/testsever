from dataclasses import field
from pyexpat import model
from django.forms import ModelForm
from django import forms
from .models import Post,Comment

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('author','comment_text',)

