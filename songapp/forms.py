from django import forms
from .models import Bills

class DateInput(forms.DateInput):
    input_type='date'

class Upload_Form(forms.ModelForm):
    class Meta:
        model=Bills
        fields=[
        "productname",
        "producttype",
        "purchasedate",
        "expirydate",
        "bill",
        "logo"
        ]
        widgets={'expirydate':DateInput(),'purchasedate':DateInput()}


        
        