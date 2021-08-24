from django import forms
from .models import *



class ProjectIdeaForm(forms.ModelForm):
    class Meta:
        model = ProjectIdea
        fields = ['projectName','projectSurname','projectNumber','projectPName','projectDescription',]

        widgets = {
            'projectName': forms.TextInput(attrs={'class':'form-control'}),
            'projectSurname': forms.TextInput(attrs={'class':'form-control'}),
            'projectNumber': forms.NumberInput(attrs={'class':'form-control','maxlength':10}),
            'projectPName': forms.TextInput(attrs={'class':'form-control'}),
            'projectDescription': forms.Textarea(attrs={'class':'form-control'}),
        }


class ProjectIdeaForm1(forms.ModelForm):
    class Meta:
        model = ProjectIdea
        fields = ['projectIsApproved', 'projectIsDenied']

        
        widgets = {
            'projectIsApproved': forms.CheckboxInput(attrs={'class':'form-control'}),
            'projectIsDenied': forms.CheckboxInput(attrs={'class':'form-control'}),
            
        }
        

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body',]

        widgets = {
            'body': forms.Textarea(attrs={'class':'form-control'}),
            
        }


class week1Form(forms.ModelForm):
    class Meta:
        model = week1
        fields = ['projectName1','projectSurname1','projectNumber1','projectPName1','projectDescription1',]

        widgets = {
            'projectName1': forms.TextInput(attrs={'class':'form-control'}),
            'projectSurname1': forms.TextInput(attrs={'class':'form-control'}),
            'projectNumber1': forms.NumberInput(attrs={'class':'form-control','maxlength':10}),
            'projectPName1': forms.TextInput(attrs={'class':'form-control'}),
            'projectDescription1': forms.Textarea(attrs={'class':'form-control'}),
        }


class week1Form1(forms.ModelForm):
    class Meta:
        model = week1
        fields = ['projectIsApproved1', 'projectIsDenied1']

        
        widgets = {
            'projectIsApproved1': forms.CheckboxInput(attrs={'class':'form-control'}),
            'projectIsDenied1': forms.CheckboxInput(attrs={'class':'form-control'}),
            
        }

class CommentForm1(forms.ModelForm):
    class Meta:
        model = Comment1
        fields = ['body',]

        widgets = {
            'body': forms.Textarea(attrs={'class':'form-control'}),
            
        }


class week2Form(forms.ModelForm):
    class Meta:
        model = Week2
        fields = ['projectName2','projectSurname2','projectNumber2','projectPName2','projectDescription2',]

        widgets = {
            'projectName2': forms.TextInput(attrs={'class':'form-control'}),
            'projectSurname2': forms.TextInput(attrs={'class':'form-control'}),
            'projectNumber2': forms.NumberInput(attrs={'class':'form-control','maxlength':10}),
            'projectPName2': forms.TextInput(attrs={'class':'form-control'}),
            'projectDescription2': forms.Textarea(attrs={'class':'form-control'}),
        }


class week2Form2(forms.ModelForm):
    class Meta:
        model = Week2
        fields = ['projectIsApproved2', 'projectIsDenied2']

        
        widgets = {
            'projectIsApproved2': forms.CheckboxInput(attrs={'class':'form-control'}),
            'projectIsDenied2': forms.CheckboxInput(attrs={'class':'form-control'}),
            
        }

class CommentForm2(forms.ModelForm):
    class Meta:
        model = Comment2
        fields = ['body',]

        widgets = {
            'body': forms.Textarea(attrs={'class':'form-control'}),
            
        }



class week3Form(forms.ModelForm):
    class Meta:
        model = Week3
        fields = ['projectName3','projectSurname3','projectNumber3','projectPName3','projectDescription3',]

        widgets = {
            'projectName3': forms.TextInput(attrs={'class':'form-control'}),
            'projectSurname3': forms.TextInput(attrs={'class':'form-control'}),
            'projectNumber3': forms.NumberInput(attrs={'class':'form-control','maxlength':10}),
            'projectPName3': forms.TextInput(attrs={'class':'form-control'}),
            'projectDescription3': forms.Textarea(attrs={'class':'form-control'}),
        }


class week3Form3(forms.ModelForm):
    class Meta:
        model = Week3
        fields = ['projectIsApproved3', 'projectIsDenied3']

        
        widgets = {
            'projectIsApproved3': forms.CheckboxInput(attrs={'class':'form-control'}),
            'projectIsDenied3': forms.CheckboxInput(attrs={'class':'form-control'}),
            
        }

class CommentForm3(forms.ModelForm):
    class Meta:
        model = Comment3
        fields = ['body',]

        widgets = {
            'body': forms.Textarea(attrs={'class':'form-control'}),
            
        }


class week4Form(forms.ModelForm):
    class Meta:
        model = Week4
        fields = ['projectName4','projectSurname4','projectNumber4','projectPName4','projectDescription4',]

        widgets = {
            'projectName4': forms.TextInput(attrs={'class':'form-control'}),
            'projectSurname4': forms.TextInput(attrs={'class':'form-control'}),
            'projectNumber4': forms.NumberInput(attrs={'class':'form-control','maxlength':10}),
            'projectPName4': forms.TextInput(attrs={'class':'form-control'}),
            'projectDescription4': forms.Textarea(attrs={'class':'form-control'}),
        }

class week4Form4(forms.ModelForm):
    class Meta:
        model = Week4
        fields = ['projectIsApproved4', 'projectIsDenied4']
      
        widgets = {
            'projectIsApproved4': forms.CheckboxInput(attrs={'class':'form-control'}),
            'projectIsDenied4': forms.CheckboxInput(attrs={'class':'form-control'}),           
        }

class CommentForm4(forms.ModelForm):
    class Meta:
        model = Comment4
        fields = ['body',]

        widgets = {
            'body': forms.Textarea(attrs={'class':'form-control'}),
            
        }


class week5Form(forms.ModelForm):
    class Meta:
        model = Week5
        fields = ['projectName5','projectSurname5','projectNumber5','projectPName5','projectDescription5',]

        widgets = {
            'projectName5': forms.TextInput(attrs={'class':'form-control'}),
            'projectSurname5': forms.TextInput(attrs={'class':'form-control'}),
            'projectNumber5': forms.NumberInput(attrs={'class':'form-control','maxlength':10}),
            'projectPName5': forms.TextInput(attrs={'class':'form-control'}),
            'projectDescription5': forms.Textarea(attrs={'class':'form-control'}),
        }

class week5Form5(forms.ModelForm):
    class Meta:
        model = Week5
        fields = ['projectIsApproved5', 'projectIsDenied5']
      
        widgets = {
            'projectIsApproved5': forms.CheckboxInput(attrs={'class':'form-control'}),
            'projectIsDenied5': forms.CheckboxInput(attrs={'class':'form-control'}),           
        }

class CommentForm5(forms.ModelForm):
    class Meta:
        model = Comment5
        fields = ['body',]

        widgets = {
            'body': forms.Textarea(attrs={'class':'form-control'}),
            
        }


class week6Form(forms.ModelForm):
    class Meta:
        model = Week6
        fields = ['projectName6','projectSurname6','projectNumber6','projectPName6','projectDescription6',]

        widgets = {
            'projectName6': forms.TextInput(attrs={'class':'form-control'}),
            'projectSurname6': forms.TextInput(attrs={'class':'form-control'}),
            'projectNumber6': forms.NumberInput(attrs={'class':'form-control','maxlength':10}),
            'projectPName6': forms.TextInput(attrs={'class':'form-control'}),
            'projectDescription6': forms.Textarea(attrs={'class':'form-control'}),
        }

class week6Form6(forms.ModelForm):
    class Meta:
        model = Week6
        fields = ['projectIsApproved6', 'projectIsDenied6']
      
        widgets = {
            'projectIsApproved6': forms.CheckboxInput(attrs={'class':'form-control'}),
            'projectIsDenied6': forms.CheckboxInput(attrs={'class':'form-control'}),           
        }

class CommentForm6(forms.ModelForm):
    class Meta:
        model = Comment6
        fields = ['body',]

        widgets = {
            'body': forms.Textarea(attrs={'class':'form-control'}),
            
        }

class week7Form(forms.ModelForm):
    class Meta:
        model = Week7
        fields = ['projectName7','projectSurname7','projectNumber7','projectPName7','projectDescription7',]

        widgets = {
            'projectName7': forms.TextInput(attrs={'class':'form-control'}),
            'projectSurname7': forms.TextInput(attrs={'class':'form-control'}),
            'projectNumber7': forms.NumberInput(attrs={'class':'form-control','maxlength':10}),
            'projectPName7': forms.TextInput(attrs={'class':'form-control'}),
            'projectDescription7': forms.Textarea(attrs={'class':'form-control'}),
        }

class week7Form7(forms.ModelForm):
    class Meta:
        model = Week7
        fields = ['projectIsApproved7', 'projectIsDenied7']
      
        widgets = {
            'projectIsApproved7': forms.CheckboxInput(attrs={'class':'form-control'}),
            'projectIsDenied7': forms.CheckboxInput(attrs={'class':'form-control'}),           
        }

class CommentForm7(forms.ModelForm):
    class Meta:
        model = Comment7
        fields = ['body',]

        widgets = {
            'body': forms.Textarea(attrs={'class':'form-control'}),
            
        }

class week8Form(forms.ModelForm):
    class Meta:
        model = Week8
        fields = ['projectName8','projectSurname8','projectNumber8','projectPName8','projectDescription8',]

        widgets = {
            'projectName8': forms.TextInput(attrs={'class':'form-control'}),
            'projectSurname8': forms.TextInput(attrs={'class':'form-control'}),
            'projectNumber8': forms.NumberInput(attrs={'class':'form-control','maxlength':10}),
            'projectPName8': forms.TextInput(attrs={'class':'form-control'}),
            'projectDescription8': forms.Textarea(attrs={'class':'form-control'}),
        }

class week8Form8(forms.ModelForm):
    class Meta:
        model = Week8
        fields = ['projectIsApproved8', 'projectIsDenied8']
      
        widgets = {
            'projectIsApproved8': forms.CheckboxInput(attrs={'class':'form-control'}),
            'projectIsDenied8': forms.CheckboxInput(attrs={'class':'form-control'}),           
        }

class CommentForm8(forms.ModelForm):
    class Meta:
        model = Comment8
        fields = ['body',]

        widgets = {
            'body': forms.Textarea(attrs={'class':'form-control'}),
            
        }