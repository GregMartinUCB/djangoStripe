from django.db import models
from models import SuitDetail, LineItem, Transaction, Customer
import stripe

class DataLinker():
	
	suitSave = SuitDetail()
	lineItemSave = LineItem()
	transactionSave = Transaction()
	customerSave = Customer()
	
	suitReady = False
	lineItemReady = False
	transactionReady = False
	customerReady = False

	def GetMeasurements(self, suit):
		
		DataLinker.suitSave = suit

	def GetTransactionData(self, stripeToken):
		return

	def SaveData(self):
		"""
		if suitReady && lineItemReady && transactionReady && customerReady:

			DataLinker.suitSave.save()
			DataLinker.ResetAll()
		"""
		DataLinker.suitSave.save()
		self.ResetAll()

	def CheckReady(self):
		suitTemp = SuitDetail()
		lineItemTemp = LineItem()
		transactionTemp = Transaction()
		customerTemp = Customer()

		if suitTemp != suitSave:
			suitReady = True
		if lineItemTemp != lineItemSave:
			lineItemReady = True
		if transactionTemp != transactionSave:
			transactionReady = True
		if customerTemp != customerSave:
			customerReady = True


	def ResetAll(self):
		
		suitReady = False
		lineItemReady = False
		transactionReady = False
		customerReady = False

		suitSave = SuitDetail()
		lineItemSave = LineItem()
		transactionSave = Transaction()
		customerSave = Customer()

		 