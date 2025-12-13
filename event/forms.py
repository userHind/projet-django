from django import forms
from .models import Birth, Death, Wedding , OfficierEtatCivil, BureauEtatCivil, RegistreNaissances, RegistreMariages, RegistreDecés


class BirthForm(forms.ModelForm):
    class Meta:
        model = Birth
        fields = '__all__'
      
    

class DeathForm(forms.ModelForm):
    class Meta:
        model = Death
        fields = '__all__'  # fields = ['username', 'password']
 
#disabled=true ---- write access denied
#help_text secrit sous le box pour expliquer
#required ----non obligatoire
class WeddingForm(forms.ModelForm):
    class Meta:
        model = Wedding
        fields = '__all__'  # fields = ['username', 'password']
        
class RegistreNForm(forms.ModelForm):
    class Meta:
        model = RegistreNaissances
        fields = '__all__'  # fields = ['username', 'password']
class BureauEtatCivilForm(forms.ModelForm):
    class Meta:
        model = BureauEtatCivil
        fields = '__all__'  # fields = ['username', 'password']
      
class OfficierEtatCivilForm(forms.ModelForm):
    class Meta:
        model = OfficierEtatCivil
        fields = '__all__'  # fields = ['username', 'password']
class RegistreMariagesForm(forms.ModelForm):
    class Meta:
        model = RegistreMariages
        fields = '__all__'  # fields = ['username', 'password']
        
class RegistreDecésForm(forms.ModelForm):
    class Meta:
        model = RegistreDecés
        fields = '__all__'  # fields = ['username', 'password']