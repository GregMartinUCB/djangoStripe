from django.shortcuts import render, redirect
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
			request.session['suitInstance'] = suitModelInstance

			return redirect('pay')
		
	else:
		form = SuitForm()



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
        #Store transaction data
        dataLinker = DataLinker()
        dataLinker.GetAllData(postData, total, request.session['suitInstance'])




    return render(request, 'Store/index.html', {'total':total})

def GetApiKey():
	module_dir = os.path.dirname(__file__)  # get current directory
	file_path = os.path.join(module_dir, 'secretKey.txt')
	with open(file_path, 'r') as f:
		stripe.api_key = f.read()
	