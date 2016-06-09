from django.shortcuts import render
from django.core.context_processors import csrf
from django.http import HttpResponse
from django.template import loader
from .measurementForm import MeasurementForm
from models import SuitForm
from stripeForm import StripeForm
from django.http import HttpResponseRedirect
from models import SuitDetail, Transaction
import stripe
from dataLinker import DataLinker
import os



def Measurements(request):
	
	
	if request.method == "POST":
		form = SuitForm(request.POST)
		print "Method is POST"
		if form.is_valid():
			print "Form is valid"
			
			suitModelInstance = form.save(commit = False)
			dataLinker = DataLinker()
			dataLinker.GetMeasurements(suitModelInstance)

			return HttpResponseRedirect('buy/')
		
	else:
		form = MeasurementForm()



	return render(request, 'Store/measurements.html', {'form': form})


def StripePay(request):
	
	#Get Secret key from file which is ignored in Git
	GetApiKey()
	
	#Check the POST for a stripe token
	if 'stripeToken' in request.POST:
		postData = request.POST
		 
		#Print out all data held in post, for debugging purposes
		for key, value in postData.items():
			print (key,value)

		token = request.POST['stripeToken']

		#ChargeSuccessful should only become true when the try statement
		#either succeeds or an error other than CardError is thrown.
		chargeSuccessful = False
		try:
			charge = stripe.Charge.create(
					 amount = 50000, #In Cents
					 currency = "usd",
					 source = token,
					 description = "Test Charge"
			)
			print "Card Charged"
			chargeSuccessful = True
	
		except stripe.error.CardError as e:
			#The card has been declined Maybe put in an email function
			chargeSuccessful =False
			pass

		#Put all the collected data together and if it passes test Save.
		if chargeSuccessful:
			dataLinker = DataLinker()
			dataLinker.GetTransactionData(token)
			dataLinker.SaveData()


	return render(request, 'Store/index.html')

def GetApiKey():
	module_dir = os.path.dirname(__file__)  # get current directory
	file_path = os.path.join(module_dir, 'secretKey.txt')
	with open(file_path, 'r') as f:
		stripe.api_key = f.read()
	