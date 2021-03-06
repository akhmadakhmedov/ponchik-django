from django import forms
from .models import Account

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter password'
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm password'
    }))
    class Meta:
        model = Account
        fields = ['name', 'surname', 'phone_number', 'email', 'password']
    
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self). __init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Enter your name'
        self.fields['surname'].widget.attrs['placeholder'] = 'Enter your surname'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter your email'
        self.fields['phone_number'].widget.attrs['placeholder'] = 'Enter your phone_number'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
    
    def clean(self):
        cleaned_data     = super(RegistrationForm, self).clean()
        password         = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password!=confirm_password:
            raise forms.ValidationError('Passwords does not match!')

        
    