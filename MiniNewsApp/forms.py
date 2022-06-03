
from .models import Blogs
from django.forms import ModelForm
from django import forms


class FormBlog(ModelForm):
    class Meta:
        model = Blogs
        fields = ['Blog_Tittle', 'Blog_Description', 'Blog_AuthorName']

    Blog_Tittle = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    Blog_Description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control'}))
    Blog_AuthorName = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
