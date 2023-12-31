from django.db import models

# Create your models here.
class Patient(models.Model):
    FirstName = models.CharField(max_length=15)
    LastName= models.CharField(max_length=15)
    UserName = models.CharField(max_length=15)
    Email = models.EmailField()
    Password = models.CharField(max_length=12)
    ConfirmPassword = models.CharField(max_length=12)
    Address = models.CharField(max_length=100)
    ProfilePicture = models.ImageField()
    def __str__(self):
        return self.UserName
    
class Doctor(models.Model):
    FirstName = models.CharField(max_length=15)
    LastName= models.CharField(max_length=15)
    UserName = models.CharField(max_length=15)
    Email = models.EmailField()
    Password = models.CharField(max_length=12)
    ConfirmPassword = models.CharField(max_length=12)
    Address = models.CharField(max_length=100)
    ProfilePicture = models.ImageField()
    def __str__(self):
        return self.UserName
class Category(models.Model):
    
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    
    title= models.CharField(max_length=100)
    image = models.ImageField( upload_to='blog/images/')
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    summary =  models.CharField(max_length=255)
    content = models.TextField()
    draft = models.BooleanField(default=False)
    

    def __str__(self):
        return self.title