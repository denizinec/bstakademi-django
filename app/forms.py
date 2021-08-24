from django import contrib, forms
from django.forms import widgets
from .models import New, Blog

class CreateNewForm(forms.ModelForm):
    class Meta:
        model = New
        fields = ["title","content","news_image"]
        widgets = {
            "title":forms.TextInput(attrs={"class":"form-control"}),
            "content":forms.Textarea(attrs={"class":"form-control"}),
        }

class CreateBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ["title","content","summary","news_image"]
        widgets = {
            "title":forms.TextInput(attrs={"class":"form-control"}),
            "content":forms.Textarea(attrs={"class":"form-control"}),
            "summary":forms.Textarea(attrs={"class":"form-control"}),
        }

class BlogFormApprov(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['IsApproved2', 'IsDenied2']

        
        widgets = {
            'IsApproved2': forms.CheckboxInput(attrs={'class':'form-control'}),
            'IsDenied2': forms.CheckboxInput(attrs={'class':'form-control'}),
            
        }
        

class Publish1(forms.ModelForm):
    class Meta:
        model = New
        fields = ['IsApproved1', 'IsDenied1']

        widgets = {
            'IsApproved1': forms.CheckboxInput(attrs={'class':'form-control'}),
            'IsDenied1': forms.CheckboxInput(attrs={'class':'form-control'}),
            
        }

