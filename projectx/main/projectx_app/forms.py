from django import forms
# Form Validation.
from django.core import validators

# Form Validation.
def check_for_m(value):
    if value[0].lower() != 'm':
        raise forms.ValidationError("Sorry, name needs to start with m")

class ContactForm(forms.Form):
    name = forms.CharField(validators=[check_for_m])
    email = forms.EmailField()
    enquiry = forms.CharField(widget=forms.Textarea)

# Form Validation.
botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])
