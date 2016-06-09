from django import forms

class MeasurementForm(forms.Form):
	color = forms.CharField(label='Color', max_length=100)
	material = forms.CharField(label='Material', max_length=100)
	lapel = forms.CharField(label='Lapel Style', max_length=100)
	fit = forms.CharField(label='Fit', max_length=100)
	chest = forms.IntegerField(label='Chest Measurement')
	waist = forms.IntegerField(label='Waist Measurement')
	inseam = forms.IntegerField(label='Inseam')
	seat = forms.IntegerField(label='Seat')
	sleeve = forms.IntegerField(label='Sleeve')
	shoulder = forms.IntegerField(label='Shoulder')
	bicep = forms.IntegerField(label='Bicep')
	front_length = forms.IntegerField(label='Front Jacket Length')
	outseam = forms.IntegerField(label='Outseam')
	thigh = forms.IntegerField(label='Thigh')

