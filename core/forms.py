from django import forms
from .models import *

class ContactFormForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['name', 'email', 'subject', 'phonenumber', 'message']




class NormalSenderForm(forms.ModelForm):
    class Meta:
        model = Normalsender
        fields = ['name', 'email', 'weight', 'phonenumber', 'address', 'description']

class NormalReceiverForm(forms.ModelForm):
    class Meta:
        model = Normalreceiver
        fields = ['name', 'email', 'phonenumber', 'address']



