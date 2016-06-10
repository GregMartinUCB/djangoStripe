from django.db import models
from models import SuitDetail, LineItem, Transaction, Customer
import stripe
import datetime

class DataLinker():
	

    def GetTransactionData(self,dataPost, amount):
        transactionModel = Transaction()
        transactionModel.stripe_token = dataPost['stripeToken']
        transactionModel.date = datetime.datetime.now()
        transactionModel.amount = amount
        transactionModel.address = dataPost['address']
        transactionModel.city = dataPost['city']
        transactionModel.zip = dataPost['zip']
        
        return transactionModel

    def GetCustomerData(self,dataPost):
        customerData = Customer()
        customerData.email = dataPost['email']
        customerData.name_last = dataPost['lastName']
        customerData.name_first = dataPost['firstName']
        
        return customerData

    def GetLineItemData(self):
        lineItem = LineItem()
        lineItem.type = "suit"
        lineItem.quantity = 1

        return lineItem


    def GetAllData(self,postData,amount,suit):

        transaction = self.GetTransactionData(postData, amount)
        customer = self.GetCustomerData(postData)
        lineItem = self.GetLineItemData()


        #Customer must be saved to generate the id value
        customer.save()
        #Now set the foreign for all those pointing to customer
        transaction.customer = customer
        lineItem.customer = customer
        suit.customer = customer

        #Repeat process: Save then Set Keys
        transaction.save()
        lineItem.transaction = transaction
        suit.transaction = transaction

        lineItem.save()
        
        suit.save()



        return

