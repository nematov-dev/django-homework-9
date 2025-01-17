from django import forms

from . import models



class ContactPageForm(forms.ModelForm):
    class Meta:
        model = models.ContactModel
        exclude = ['phone']

class ContactAboutPageForm(forms.ModelForm):
    class Meta:
        model = models.ContactModel
        exclude = ['subject']

