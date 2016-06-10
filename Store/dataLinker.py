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

    def GetTransactionData(self, dataPost, amount):
        DataLinker.transactionSave.stripe_token = dataPost['stripeToken']
        DataLinker.transactionSave.date.auto_now_add
        DataLinker.transactionSave.amount = amount
        
        
        return

    def GetCustomerData(self, dataPost):
        DataLinker.customerSave.email = dataPost['email']
        DataLinker.customerSave.name_last = dataPost['lastName']
        DataLinker.customerSave.name_first = dataPost['firstName']
        DataLinker.customerReady = True

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