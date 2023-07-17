from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Article(models.Model):
    
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=150,null=False)
    text= models.TextField()
    publish_status=models.BooleanField(default=False)

    
    def __str__(self):
        return self.title
    

class AddContent(models.Model):
    article=models.ForeignKey(Article,on_delete=models.CASCADE)
    text=models.TextField()
    image = models.ImageField(upload_to='images/',null=True)
    caption= models.CharField(max_length=50)
    
    
    


    



