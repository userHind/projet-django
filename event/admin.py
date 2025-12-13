from django.contrib import admin
from .models import Birth, Death, Wedding, OfficierEtatCivil, BureauEtatCivil, RegistreNaissances, RegistreMariages, RegistreDecés
# Register your models here.
class BirthAdmin(admin.ModelAdmin):
    #list_display = ['Nom']
    #list_display_links = ['NumRegNais', 'NumAdN','annee','Nom']
    #list_editable = ['price'] #ce qui est la ne peut pas etre un link
    search_fields = ['annee','Nom','NumAdN','NumRegNais']
    list_filter = ['annee','NumRegNais']
    fields =  ['NumAdN','Nom','Prenom','sexe','DateNaissance','HeureNaissance','annee','LieuNaissance','PaysNaissance','NomPrenomPere','DateNPere','LieuNPere','ProfessionPere','NomPrenomMere','DateNMere','LieuNMere','ProfessionMere','NomPrenomGPM','NomPrenomGPP','NomPrenomGMP','NomPrenomGMM','NumRegNais']
class DeathAdmin(admin.ModelAdmin):
    #list_display = ['Nom']
    #list_display_links = ['NumRegNais', 'NumAdN','annee','Nom']
    #list_editable = ['price'] #ce qui est la ne peut pas etre un link
    search_fields = ['annee','Nom','NumAdD','NumRegDeces']
    list_filter = ['annee','NumRegDeces']
    fields =  ['NumAdD','NumAdN','Nom','Prenom','dateD','JourDeces','HeureDeces','LieuDeces','Sexe','Marie','NumRegDeces','annee']
class WeddingAdmin(admin.ModelAdmin):
    #list_display = ['Nom']
    #list_display_links = ['NumRegNais', 'NumAdN','annee','Nom']
    #list_editable = ['price'] #ce qui est la ne peut pas etre un link
    search_fields = ['acteNaissEpx','acteNaissEpse','NumAdM','NumRegMar','DateMariage']
    list_filter = ['NumRegMar']
    fields =  ['NumAdM','acteNaissEpx','acteNaissEpse','LieuMariage','DateMariage','ProfessionF','ProfessionH','Domicile','NPTemoin1','NPTemoin2','NumRegMar']
admin.site.register(Birth, BirthAdmin) 
admin.site.register(Death, DeathAdmin) 
admin.site.register(Wedding, WeddingAdmin) 
admin.site.site_header = 'Site des Actes dEtats Civils'
admin.site.site_title = 'City hall s System Managment' 
admin.site.register(OfficierEtatCivil)
admin.site.register(BureauEtatCivil)
admin.site.register(RegistreNaissances)
admin.site.register(RegistreMariages)
admin.site.register(RegistreDecés)
    


        
        
   
 
     