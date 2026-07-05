from django import forms
from .models import Contact

class ContactModelForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'input-custom',
                'placeholder': 'Your Name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'input-custom',
                'placeholder': 'Your Email'
            }),
            'message': forms.Textarea(attrs={
                'class': 'input-custom',
                'placeholder': 'Your Message',
                'rows': 4,
            }),
        }