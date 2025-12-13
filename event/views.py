
from django.db.models import Count
from django.shortcuts import render
from .models import Birth, Death, Wedding, OfficierEtatCivil, BureauEtatCivil, RegistreNaissances, RegistreMariages, RegistreDecés
from .forms import BirthForm, DeathForm, WeddingForm, RegistreNForm,OfficierEtatCivilForm,BureauEtatCivilForm,RegistreMariagesForm,RegistreDecésForm
from datetime import datetime
from django.contrib.auth import get_user_model
from .models import Birth as birth
from .models import Death as death

 
# Create your views here.

def Birth(request):
    if request.method == 'POST':
        dataform = BirthForm(request.POST)
        if dataform.is_valid():
            dataform.save()
    return render(request, 'event/birth.html', {'bf':BirthForm})

def Wedding(request):
    if request.method == 'POST':
        dataform = WeddingForm(request.POST)
        if dataform.is_valid():
            dataform.save()
    return render(request, 'event/wedding.html', {'wf':WeddingForm})

def Death(request):
    if request.method == 'POST':
        dataform = DeathForm(request.POST)
        if dataform.is_valid():
            dataform.save()
  
    return render(request, 'event/death.html', {'df':DeathForm})



def RegistreNaissances(request):
      if request.method == 'POST':
        dataform = RegistreNForm(request.POST)
        if dataform.is_valid():
            dataform.save()
      return render(request, 'event/Bregistre.html', {'RNf':RegistreNForm})
def RegistreMariages(request):
      if request.method == 'POST':
        dataform = RegistreMariagesForm(request.POST)
        if dataform.is_valid():
            dataform.save()
      return render(request, 'event/Wregistre.html', {'RMf':RegistreMariagesForm})
def RegistreDecés(request):
      if request.method == 'POST':
        dataform = RegistreDecésForm(request.POST)
        if dataform.is_valid():
            dataform.save()
      return render(request, 'event/Dregistre.html', {'RDf':RegistreDecésForm})
  
def BureauEtatCivil(request):
      if request.method == 'POST':
        dataform = BureauEtatCivilForm(request.POST)
        if dataform.is_valid():
            dataform.save()
      return render(request, 'event/officer.html', {'Bf':BureauEtatCivilForm})
def OfficierEtatCivil(request):
      if request.method == 'POST':
        dataform = OfficierEtatCivilForm(request.POST)
        if dataform.is_valid():
            dataform.save()
      return render(request, 'event/officer.html', {'Of':OfficierEtatCivilForm})
  


def statistics(request):  
    ActesM = birth.objects.all()
    NumMajeurs = 0
    NumMineurs = 0

    for acte in ActesM:

        if datetime.today().year - int(acte.annee) > 18:
            NumMajeurs = NumMajeurs + 1
        else:
            NumMineurs = NumMineurs + 1

    statsM = NumMajeurs
    statsm = NumMineurs
    Acte = birth.objects.all()
    Act = death.objects.all()
    Actes = birth.objects.all().count()
    Actesd = death.objects.all().count()
    ActesB = birth.objects.values("annee").annotate(nombre=Count("annee"))
    ActesD = death.objects.values("annee").annotate(nombre=Count("annee"))
    context = {
        'Acte':Acte,
        'Act':Act,
        'Actes' : Actes,
        'Actesd':Actesd,
        'ActesD':ActesD,
        'ActesB':ActesB,
        'statsM':statsM,
        'statsm':statsm
        
    }
    return render(request, 'event/statistics.html',context)







#x = {'Les Statistiques des Taux de Naissances sont :':'Actes', 'Les Statistiques des Taux de Deces sont :':'ActesD', ' Les Statistiques des Majeurs et Mineurs sont :':'stats'}



