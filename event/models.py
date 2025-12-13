from django.db import models
from django.contrib.auth import get_user_model
from django import forms 
import uuid
from django.core.exceptions import ValidationError

# Create your models here.


User = get_user_model()


class OfficierEtatCivil(models.Model):
    matricule = models.UUIDField(primary_key=True, editable=False)
    nom = models.CharField(max_length=20)
    prenom = models.CharField(max_length=20)
    datePriseService = models.DateField(null=True)
    estMaire = models.BooleanField(default=False)
    Bureau = models.ForeignKey("BureauEtatCivil", null=False, on_delete=models.CASCADE)
    user = models.OneToOneField(User, null="True", on_delete=models.CASCADE)


class BureauEtatCivil(models.Model):
    estConsulat = models.BooleanField(default=False)
    Commune = models.CharField(max_length=30)
    Daira = models.CharField(max_length=30)
    Wilaya = models.CharField(max_length=30)

    class Meta:
        unique_together = ('Commune', 'Daira', 'Wilaya')


class RegistreNaissances(models.Model):
    Année = models.CharField(max_length=4)
    Bureau0 = models.ForeignKey("BureauEtatCivil", null=False, on_delete=models.CASCADE)


class RegistreMariages(models.Model):
    Année = models.CharField(max_length=4)
    Bureau1 = models.ForeignKey("BureauEtatCivil", null=False, on_delete=models.CASCADE)


class RegistreDecés(models.Model):
    Année = models.CharField(max_length=4)
    Bureau2 = models.ForeignKey("BureauEtatCivil", null=False, on_delete=models.CASCADE)


class Birth(models.Model):
       x = [
        ('H','Homme'),
        ('F','Femme'),
     ]
       NumAdN = models.CharField(max_length=50,unique=True, verbose_name='Numéro d’enregistrement')
       Nom = models.CharField(max_length=50)
       Prenom = models.CharField(max_length=50)
       sexe = models.CharField(max_length=10, choices=x, verbose_name=' Sélectionner le sexe ')
       DateNaissance = models.DateField(null=True)
       HeureNaissance = models.TimeField(null=True , verbose_name='heure de naissance')
       annee = models.CharField(max_length=4, default="" )
       LieuNaissance = models.CharField(max_length=50)
       PaysNaissance = models.CharField(max_length=50)
       NomPrenomPere = models.CharField(max_length=50 , verbose_name='Nom et Prenom du Pere')
       DateNPere = models.DateField(verbose_name='Entrez la date de naissance du Pére')
       LieuNPere = models.CharField(max_length=50, verbose_name='Entrez le lieu de naissance du Pére')
       ProfessionPere = models.CharField(max_length=50, verbose_name='Entrez la profession du Pére')
       NomPrenomMere = models.CharField(max_length=50, verbose_name='Entrez le Nom et Prénom de la Mére')
       DateNMere = models.DateField(verbose_name='Entrez la date de naissance de la Mére')
       LieuNMere = models.CharField(max_length=50, verbose_name='Entrez le lieu de naissance de la Mére')
       ProfessionMere = models.CharField(max_length=50, verbose_name='Entrez la profession de la Mére')
       NomPrenomGPP = models.CharField(max_length=50, verbose_name='Entrez le Nom et Prénom grandPére Paternel')
       NomPrenomGPM = models.CharField(max_length=50, verbose_name='Entrez le Nom et Prénom grandPére Maternel')
       NomPrenomGMP = models.CharField(max_length=50, verbose_name='Entrez le Nom et Prénom grandMére Paternel')
       NomPrenomGMM = models.CharField(max_length=50, verbose_name='Entrez le Nom et Prénom grandMére Maternel')
       NumRegNais = models.ManyToManyField(RegistreNaissances, verbose_name='Entrez le Numero du registre de naissance')
       def __str__(self):
           return self.Nom
       def save(self, *args, **kwargs):
        self.annee = self.DateNaissance.strftime('%Y')
        super(Birth, self).save(*args, **kwargs)
    

      

       
class Wedding(models.Model):
    NumAdM = models.CharField(max_length=50,verbose_name='Numéro d’enregistrement du mariage')
    acteNaissEpx = models.ForeignKey(Birth, on_delete=models.CASCADE, default='',related_name="naissEp") 
    acteNaissEpse = models.ForeignKey(Birth, on_delete=models.CASCADE,default='',related_name="naissEpse") 
    LieuMariage = models.CharField(max_length=50)
    DateMariage = models.DateField(null=True)
    ProfessionF = models.CharField(max_length=50, default="", verbose_name='Entrez la profession de la Femme')
    ProfessionH = models.CharField(max_length=50, default="", verbose_name='Entrez la profession de lHomme')
    Domicile = models.TextField(max_length=50, default="")
    NPTemoin1 = models.CharField(max_length=50, default="", verbose_name='Entrez le Nom et Prénom du temoin1')
    NPTemoin2 = models.CharField(max_length=50, default="", verbose_name='Entrez le Nom et Prénom du temoin2')
    NumRegMar = models.ManyToManyField(RegistreMariages,verbose_name='Entrez le Numero du registre du mariage')
  
    def clean(self):
        if self.acteNaissEpx.sexe != "Homme" or self.acteNaissEpse.sexe != "Femme":
            raise forms.ValidationError("sexes invalides")
    class Meta:
        unique_together = ('acteNaissEpx', 'acteNaissEpse')
    def __str__(self):
        return self.DateMariage

class Death(models.Model):
        x = [
        ('H','Homme'),
        ('F','Femme'),
        ]
        NumAdD = models.CharField(max_length=50, null=True,verbose_name='Numéro denregistrement de Deces')
        NumAdN = models.OneToOneField(Birth, null=True,on_delete=models.CASCADE , verbose_name='Numéro denregistrement')
        Nom = models.CharField(max_length=50)
        Prenom = models.CharField(max_length=50)
        dateD = models.DateField(max_length=4,null=True) 
        JourDeces = models.CharField(max_length=15)
        HeureDeces = models.CharField(max_length=2)
        LieuDeces = models.CharField(max_length=50)
        Sexe = models.CharField(max_length=50 ,choices=x)
        Marie = models.CharField(max_length=50)
        NumRegDeces = models.ManyToManyField(RegistreDecés,max_length=50)
        annee = models.CharField(max_length=4,  default="")
        def __str__(self):
               return self.Nom
        def save(self, *args, **kwargs):
            self.annee = self.dateD.strftime('%Y')
            super(Death, self).save(*args, **kwargs)










