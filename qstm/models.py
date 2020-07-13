from django.db import models
from datetime import datetime, timedelta

class User(models.Model):
    user_id     = models.AutoField(primary_key=True)    
    user_username   = models.CharField(max_length=30, unique=False)
    password    = models.CharField(max_length=30, unique=False)
    is_parent   = models.BooleanField(default=True)
    last_login  = models.DateField(auto_now=True)
    is_active   = models.BooleanField(default=True)
    
    def __str__(self):
      return self.user_username

class Parent(models.Model):
    parent_id     = models.AutoField(primary_key=True)    
    user_id       = models.ForeignKey(User, on_delete=models.CASCADE)
    email         = models.EmailField(max_length=60, unique=True, blank=True, null=True)
    name          = models.CharField(max_length=60, unique=False)
    cellphone     = models.CharField(max_length=12, blank=True, null=True)

    def __str__(self):
      return self.name

class Student(models.Model):
    student_id    = models.AutoField(primary_key=True)    
    user_id       = models.ForeignKey(User, on_delete=models.CASCADE)
    parent_id     = models.ForeignKey(Parent, on_delete=models.CASCADE)
    name          = models.CharField(max_length=60, unique=False)

    def __str__(self):
      return self.name


def get_due_date():
        # return datetime.today() + timedelta(days=3)     
        return (datetime.today() + timedelta(days=3)).date()    
      
      

class Task(models.Model):
    PRIORITY_OPTIONS = (
        ('U', 'Urgent'),
        ('I', 'Important'),
        ('N', 'Normal'),
        ('L', 'Low'),
    )

    task_id         = models.AutoField(primary_key=True)    
    student_id      = models.ForeignKey(Student, on_delete=models.CASCADE)
    date_created  	= models.DateField(auto_now=True)
    due_date        = models.DateField(default=get_due_date)
    class_topic	    = models.CharField(max_length=250, blank=True, null=True, verbose_name='Class')
    description		  = models.CharField(max_length=250, blank=True, null=True)
    priority        = models.CharField(max_length=1, choices=PRIORITY_OPTIONS, default='N')
    completed		    = models.BooleanField(default=False)
    date_completed	= models.DateField(blank=True, null=True)

    def __str__(self):
      return self.class_topic

class Site(models.Model):
    site_id         = models.AutoField(primary_key=True)    
    student_id      = models.ForeignKey(Student, on_delete=models.CASCADE)
    site_url        = models.CharField(max_length=2083, blank=False, null=False)
    site_username   = models.CharField(max_length=100, blank=False, null=False)
    site_password   = models.CharField(max_length=100, blank=False, null=False)
    class_topic     = models.CharField(max_length=100, blank=False, null=False)

    
    