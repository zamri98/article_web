from django import forms
from .models import *
from django.contrib.auth.models import User


class ArticleForm(forms.ModelForm):
    
    class Meta:
        
        model=Article
        
        fields=["title","text"]
        

class ImageForm(forms.ModelForm):
    
    
        class Meta:
        
            model=ImageUpload
            
            fields=["image","caption"]
            
    