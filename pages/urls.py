from django.urls import path
from . import views
 
urlpatterns = [
 path('', views.index, name='index'),
 path('about', views.about, name='about'),
 path('update', views.update, name='update'),
]
# we write 'index'  >> pages/index