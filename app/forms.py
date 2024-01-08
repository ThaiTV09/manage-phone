from django import forms
from app.models import Phone

class PhoneForm(forms.ModelForm):
    class Meta:
        model = Phone
        fields = ['phone', 'serial', 'pack', 'money', 'date_connect', 'department_id', 'date_join', 'status_id', 'system_id', 'network_id']
        widgets = {'phone': forms.TextInput(attrs={'class': 'form-control'}),
                   'serial': forms.TextInput(attrs={'class': 'form-control'}),
                   'pack': forms.TextInput(attrs={'class': 'form-control'}),
                   'money': forms.TextInput(attrs={'class': 'form-control'}),
                   'date_connect': forms.DateInput(attrs={'class': 'form-control', 'placeholder':'Select a date','type': 'date', }),
                   'department_id': forms.Select(attrs={'class': 'form-control'}),
                   'date_join': forms.DateInput(attrs={'type': 'date', 'placeholder':'Select a date', 'class': 'form-control'}),    
                   'status_id': forms.Select(attrs={'class': 'form-control'}),
                   'system_id': forms.Select(attrs={'class': 'form-control'}),                   
                   'network_id': forms.Select(attrs={'class': 'form-control'}),
                   }
        
class PhoneFormUpdate(forms.ModelForm):
    class Meta:
        model = Phone
        fields = [ 'serial', 'pack', 'money', 'department_id', 'date_join', 'status_id', 'system_id']
        widgets = {'serial': forms.TextInput(attrs={'class': 'form-control'}),
                   'pack': forms.TextInput(attrs={'class': 'form-control'}),
                   'money': forms.TextInput(attrs={'class': 'form-control'}),
                   'department_id': forms.Select(attrs={'class': 'form-control'}),
                   'date_join': forms.DateInput(attrs={'type': 'date', 'placeholder':'Select a date', 'class': 'form-control'}),    
                   'status_id': forms.Select(attrs={'class': 'form-control'}),
                   'system_id': forms.Select(attrs={'class': 'form-control'}),
                   }