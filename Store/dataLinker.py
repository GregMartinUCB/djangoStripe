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
        DataLinker.transactionSave.address = dataPost['address']
        DataLinker.transactionSave.city = dataPost['city']
        DataLinker.transactionSave.zip = dataPost['zip']
        
        return

    def GetCustomerData(self, dataPost):
        DataLinker.customerSave.email = dataPost['email']
        DataLinker.customerSave.name_last = dataPost['lastName']
        DataLinker.customerSave.name_first = dataPost['firstName']
        DataLinker.customerReady = True

    def GetLineItemData(self):
        DataLinker.lineItemSave.type = "suit"
        DataLinker.lineItemSave.quantity = 1

    def LinkData(self,customerPk, transactionPk, lineItemPk):
        DataLinker.suitSave.customer = customerPk
        DataLinker.suitSave.lineItem = lineItemPk
        DataLinker.suitReady = True

        DataLinker.lineItemSave.transaction = transactionPk
        DataLinker.lineItemReady = True

        DataLinker.transactionSave.customer = customerPk
        DataLinker.transactionReady = True

    def SaveData(self):
	        

        if (suitReady and lineItemReady and transactionReady and customerReady):

            DataLinker.suitSave.save()
            DataLinker.transactionSave.save()
            DataLinker.customerSave.save()
            DataLinker.lineItemSave.save()
            DataLinker.ResetAll()
	    
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