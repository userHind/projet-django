from django import forms
from .models import Login

class LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = '__all__'  # fields = ['username', 'password']

 
#disabled=true ---- write access denied
#help_text secrit sous le box pour expliquer
#required ----non obligatoire