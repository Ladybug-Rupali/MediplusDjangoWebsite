from WebAsha.models import *
from django import forms


class bookingForm(forms.ModelForm):
    class Meta:
        model = booking
        fields = ['name', 'email', 'phone', 'date', 'time', 'disease']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),  # HTML5 date picker
            'time': forms.TimeInput(attrs={'type': 'time'}),  # HTML5 time picker
        }


class NewsletterSubscriptionForm(forms.ModelForm):
    class Meta:
        model = NewsletterSubscription
        fields = ['email']