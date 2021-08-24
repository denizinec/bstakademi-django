from django import forms
from .models import *



class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name','surname','school_n','school','email','phone_n','bio','skills']

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'surname': forms.TextInput(attrs={'class':'form-control'}),
            'school_n': forms.NumberInput(attrs={'class':'form-control','maxlength':10}),
            'school': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
            'phone_n': forms.NumberInput(attrs={'class':'form-control','maxlength':10}),
            'bio': forms.TextInput(attrs={'class':'form-control','maxlength':100}),
        }