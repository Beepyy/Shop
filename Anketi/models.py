from django.db import models

class Skill(models.Model):
    Name=models.CharField(max_length=20)
    person=models.ForeignKey('Person',on_delete=models.SET_DEFAULT,default=None)
    percent=models.IntegerField()
    description=models.TextField()

    def __str__(self):
        return self.Name


class Person(models.Model):
    First_Name=models.CharField(max_length=20)
    Second_Name=models.CharField(max_length=20)
    Photo=models.ImageField()
    About_yourself=models.TextField(max_length=250)
    phone_number=models.IntegerField()


    def __str__(self):
        return self.First_Name