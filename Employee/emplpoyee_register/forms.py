from django import forms
from .models import create
class Employee_form(forms.ModelForm):
    class Meta:
        model=create
        fields=[
            'name',
            'title',
            'age',
            'postion'
        ]
