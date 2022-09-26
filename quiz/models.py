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


class Question(models.Model):
    
    SCALE = {
        ('B','Beginner'),
        ('I','Intermediate'),
        ('A','Advance')
    }
    
    title = models.TextField()
    quiz = models.ForeignKey(Quiz,on_delete=models.CASCADE)
    difficulty =models.CharField(max_length=1,choices=SCALE)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now_add=True)
    
class Options(models.Model):
    option_text = models.CharField(max_length=200)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)