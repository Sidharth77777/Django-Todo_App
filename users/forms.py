from django import forms
from .models import CustomUser

class CustomUserCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(
        attrs = {
            'placeholder' : 'Enter the password',
        }
    ))
    full_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter your full name',
    }))
    email = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter your email',
    }))
    

    class Meta:
        model = CustomUser
        fields = ['email', 'full_name', 'user_class', 'user_division', 'password']
