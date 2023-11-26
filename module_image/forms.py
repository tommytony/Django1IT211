from django import forms
from django.forms import ModelForm
from .models import Post


# Create a venue form 
class PostForm(ModelForm):
    class Meta:
        model=Post
        fields=('titled', 'photo', 'description')
        
        labels={
            'titled': 'Enter Your Venue Here:',
            'photo':'',
            'description':'',
            
        }
        
        widgets={
            'titled': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Titled' }),
            'description':forms.TextInput(attrs={'class': 'form-control', 'placeholder':'description'}),
            
        }