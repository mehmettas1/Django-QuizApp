from msilib.schema import Class
from tabnanny import verbose
from turtle import title
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Categories'
        
class Quiz(models.Model):
    title= models.CharField(max_length=50,verbose_name='Quiz title')
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now_add=True)
    
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Quizes'


class Question(models.Model)