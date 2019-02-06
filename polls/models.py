from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    email = models.EmailField()
    password = models.CharField(max_length=40)
    age = models.CharField(max_length=50)
    subject = models.CharField(max_length=100)


    def __str__(self):
        return self.name


class Books(models.Model):
    book_name = models.CharField(max_length=100)
    author = models.CharField(max_length=120)
    pages = models.IntegerField()
    pub_date = models.DateField()

    def __str__(self):
        return self.book_name


class Author(models.Model):
    auther_name = models.CharField(max_length=120)
    writing_exp = models.IntegerField()

    def __str__(self):
        return self.auther_name