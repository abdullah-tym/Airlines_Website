import email
from enum import auto
from http import client
from pyexpat import model
from random import random
from tkinter import CASCADE
from unicodedata import name
from django.db import models
from django.forms import EmailField, PasswordInput
from django.contrib.auth.models import User

# Create your models here.

class Utilisateur(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    myphone = models.CharField(max_length=80)

class Avion(models.Model):
    nomav = models.CharField(max_length=30, primary_key = True)
    modelav = models.CharField(max_length=30)
    capacite = models.IntegerField()
    def __str__(self):
        return self.nomav

class Voyage(models.Model):
    voyid = models.CharField(max_length=20, primary_key= True)
    depart = models.CharField(max_length=30,)
    destination = models.CharField(max_length=30)
    datedep = models.DateTimeField()
    avion = models.ForeignKey("Avion", on_delete=models.CASCADE)
    def __str__(self):
        return self.voyid


class Contact(models.Model):
    #creating an automatic field using a function called build_id
    num = models.AutoField(primary_key=True, auto_created=True)
    mail = models.EmailField()
    phone = models.CharField(max_length=15)
    msg = models.CharField(max_length=150)
    client = models.ForeignKey("Utilisateur", on_delete=models.CASCADE)

class Reserve(models.Model):
    client = models.ForeignKey("Utilisateur", on_delete=models.CASCADE)
    voy = models.ForeignKey("Voyage", on_delete=models.CASCADE)



######################################################################################################################


class Flight(models.Model):
    airline = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

class Seat(models.Model):

	CLASS_TYPE_CHOICES = [
    ('economy', 'Economy'),
    ('business', 'Business'),
    ('first', 'First'),
	]


	seat_number = models.CharField(max_length=5, default=1)
	row = models.CharField(max_length=1, default='A')
	column = models.CharField(max_length=1, default=1)
	class_type = models.CharField(max_length=10, choices=CLASS_TYPE_CHOICES, default='Economy')
	is_booked = models.BooleanField(default=False)
	flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name='seats', default=1)

	def __str__(self):
	    return f'{self.seat_number} ({self.class_type})'



######################################################################################################################


# from django.db import models

# class Movie(models.Model):
#     title=models.CharField(max_length=255)
#     price=models.IntegerField()
#     booked_seats=models.ManyToManyField('Seat',blank=True)
#     created=models.DateTimeField(auto_now_add=True)

#     def __str__(self) -> str:
#         return f"{self.title} (${self.price})"

# class Seat(models.Model):
#     seat_no=models.IntegerField()
#     occupant_first_name=models.CharField(max_length=255)     
#     occupant_last_name=models.CharField(max_length=255)     
#     occupant_email=models.EmailField(max_length=555)     
#     purchase_time=models.DateTimeField(auto_now_add=True)

#     def __str__(self) -> str:
#         return f"{self.occupant_first_name}-{self.occupant_last_name} seat_no {self.seat_no}"
#         