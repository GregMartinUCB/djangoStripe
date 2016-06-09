from __future__ import unicode_literals

from django.db import models
from django.forms import ModelForm


class Customer(models.Model):
	name = models.CharField(max_length = 100)
	email = models.EmailField()

class Transaction(models.Model):
	stripe_token = models.CharField(max_length=200)
	date = models.DateTimeField('date of transaction')
	amount = models.FloatField(default = 0)
	customer = models.ForeignKey(Customer, default = -1, on_delete = models.CASCADE)

class LineItem(models.Model):
	type = models.CharField(max_length=50)
	quantity = models.IntegerField()
	customer = models.ForeignKey(Customer, default = -1, on_delete = models.CASCADE)
	transaction = models.ForeignKey(Transaction, on_delete = models.CASCADE)
	
class SuitDetail(models.Model):
	
	
	color = models.CharField(default = -1,max_length=25)
	material = models.CharField(default = -1,max_length=25)
	lapel = models.CharField(default = -1,max_length=25)
	fit = models.CharField(default = -1,max_length=25)
	chest = models.IntegerField(default = -1)
	waist = models.IntegerField(default = -1)
	inseam = models.IntegerField(default = -1)
	seat = models.IntegerField(default = -1)
	sleeve = models.IntegerField(default = -1)
	shoulder = models.IntegerField(default = -1)
	bicep = models.IntegerField(default = -1)
	front_length = models.IntegerField(default = -1)
	outseam = models.IntegerField(default = -1)
	thigh = models.IntegerField(default = -1)
	crotch = models.IntegerField(default = -1)
	hip = models.IntegerField(default = -1)
	customer = models.ForeignKey(Customer, default = -1, on_delete = models.CASCADE)
	lineItem = models.ForeignKey(LineItem, default = -1, on_delete = models.CASCADE)

class SuitForm(ModelForm):
	class Meta:
		model = SuitDetail
		fields = [ 'color', 'material','lapel', 'fit',
				   'chest', 'waist', 'inseam', 'seat',
				  'sleeve', 'shoulder', 'bicep', 'front_length',
				  'outseam', 'thigh', 'crotch', 'hip']












