from django import forms
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class UniversityForm(forms.Form):
  name=forms.CharField(label='Product name')
      

 


#  date_of_birth=forms.DateField()
 