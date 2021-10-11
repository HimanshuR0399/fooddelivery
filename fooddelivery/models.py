from django.db import models
from django.db.models.base import Model
from django.db.models.constraints import CheckConstraint
from django.db.models.fields import files

# Create your models here.

class Users(models.Model):
    username = models.CharField(max_length=30,null=False,unique=True)
    name = models.CharField(max_length=50,null= False)
    gender = models.CharField(max_length=1,null=False)
    contact = models.CharField(max_length=10)
    is_chef = models.BooleanField(default=False)
    photo = models.CharField(max_length=40,null= True)
    def __str__(self) -> str:
        return self.username

class Addresses(models.Model):
    username = models.ForeignKey(Users, on_delete= models.CASCADE)
    address = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.username.username +' - '+self.address

class Payments(models.Model):
    username = models.ForeignKey(Users,on_delete=models.CASCADE)
    type = models.CharField(max_length=10)
    field1 = models.CharField(max_length=50)
    field2 = models.CharField(max_length=50)
    field3 = models.CharField(max_length=50)
    field4 = models.CharField(max_length=50)
    field5 = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.username.username

class Foods(models.Model):
    name = models.CharField(max_length=20)
    photo = models.CharField(max_length=40)
    calorie = models.FloatField()
    fats = models.FloatField()
    carbs = models.FloatField()
    protien = models.FloatField()
    addn_nuti_info = models.CharField(max_length=25)
    description = models.CharField(max_length=1000)
    avilability = models.BooleanField()
    prise = models.IntegerField(default=0)
    chef = models.ForeignKey(Users, on_delete = models.CASCADE)


    def __str__(self) -> str:
        return self.name + ' by ' + self.chef.username

class Orders(models.Model):
    Amount = models.FloatField()
    payment_mode = models.CharField(max_length=3)
    paid = models.BooleanField()
    delivery_address = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=10)
    transaction_no = models.CharField(max_length=30)
    status = models.IntegerField(default=0)
    user_profile = models.ForeignKey(Users, on_delete=models.NOT_PROVIDED)


class Reviews(models.Model):
    user = models.ForeignKey(Users, on_delete = models.CASCADE)
    food = models.ForeignKey(Foods, on_delete = models.CASCADE)
    stars = models.IntegerField()
    review = models.CharField(max_length= 200)

class Cart(models.Model):
    user = models.ForeignKey(Users,on_delete=models.CASCADE)
    food = models.ForeignKey(Foods, on_delete = models.CASCADE)
    quantity = models.IntegerField(default=1)

class FoodOrdered(models.Model):
    order = models.ForeignKey(Orders, on_delete = models.CASCADE)
    food = models.ForeignKey(Foods, on_delete = models.CASCADE)
    quantity = models.IntegerField(default=1)




    

    

