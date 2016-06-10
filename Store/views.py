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
    total = 510
    #Get Secret key from file which is ignored in Git
    GetApiKey()
    chargeSuccessful = False

    postData = request.POST
    #Print out all data held in post, for debugging purposes
    

	#Check the POST for a stripe token
    if 'stripeToken' in request.POST:
        postData = request.POST
		 
    #Print out all data held in post, for debugging purposes
        for key, value in postData.items():
            print (key,value)

        token = request.POST['stripeToken']
        """
        for key, value in postData.items():
            print (key,value)
        """
        #Put all the collected data together and if it passes test Save.
        dataLinker = DataLinker()
        dataLinker.GetTransactionData(token, amount)
        dataLinker.GetCustomerData(postData)
        dataLinker.GetLineItemData()
        dataLinker.LinkData()
        dataLinker.SaveData()




    return render(request, 'Store/index.html', {'total':total})

def GetApiKey():
	module_dir = os.path.dirname(__file__)  # get current directory
	file_path = os.path.join(module_dir, 'secretKey.txt')
	with open(file_path, 'r') as f:
		stripe.api_key = f.read()
	