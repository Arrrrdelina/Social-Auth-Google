from .models import Profile
from django.forms import ModelForm, TextInput


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ["name", "email"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your name'
            }),

            "email": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email'
            }),
        }