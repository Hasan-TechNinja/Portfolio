from django import forms
from .models import Contact

class ContactModelForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'block w-full px-5 py-4 bg-slate-50 border-none rounded-2xl focus:ring-2 focus:ring-brand-500 transition-all text-slate-900 placeholder:text-slate-400',
                'placeholder': 'Your Name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'block w-full px-5 py-4 bg-slate-50 border-none rounded-2xl focus:ring-2 focus:ring-brand-500 transition-all text-slate-900 placeholder:text-slate-400',
                'placeholder': 'Your Email'
            }),
            'message': forms.Textarea(attrs={
                'class': 'block w-full px-5 py-4 bg-slate-50 border-none rounded-2xl focus:ring-2 focus:ring-brand-500 transition-all text-slate-900 placeholder:text-slate-400',
                'placeholder': 'Your Message',
                'rows': 4,
            }),
        }