from django import forms
from itmgmt.models import *

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields=[
            'login','password','name','email','mobile','department'
        ]
        widgets = {
            'password' : forms.PasswordInput()
        }


