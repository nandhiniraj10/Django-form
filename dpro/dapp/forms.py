from django import forms
from .models import Person

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'email','age']

# from django import forms  
# class StudentForm(forms.Form):  
#     firstname = forms.CharField(label="enter first name",max_length=50)  
#     lastname  = forms.CharField(label="Enter last name", max_length = 100)

# yourapp/views.py


