 

from .models import Task
from django import forms

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields= ['title','description','important']
        widgets= {
            'title': forms.TextInput(attrs={'class':'form-control','placeholder':'Escribe tu titulo'}),
            'description': forms.Textarea(attrs={'class':'form-control','placeholder':'Escribe tu titulo'}),
            'important': forms.CheckboxInput(attrs={'class':'form-check-input'}),
        }