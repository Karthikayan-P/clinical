from django import forms
from .models import clinicuser

class clinicform(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = clinicuser
        fields = ['username', 'password', 'role']