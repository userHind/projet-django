from django.urls import path
from . import views
 
urlpatterns = [
   # path('', views.Event, name='event'),
    path('birth', views.Birth, name='birth'),
    path('death', views.Death, name='death'),
    path('wedding', views.Wedding, name='wedding'),
    path('statistics', views.statistics, name='statistics'),
    path('bureau', views.BureauEtatCivil, name='bureau'),
    path('officer', views.OfficierEtatCivil, name='officer'),
    path('Wregistre', views.RegistreMariages, name='Wregistre'),
    path('Dregistre', views.RegistreDecés, name='Dregistre'),
    path('Bregistre', views.RegistreNaissances, name='Bregistre'),

]
# we write 'index'  >> pages/index