from django.shortcuts import render
from .models import Login
from .forms import LoginForm
 # from django.http import HttpResponse 
 
# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

# si affichage httpresponse('helloworld')
 
def update(request):
    return render(request, 'pages/update.html')

def about(request):
   # if request.method == 'POST':
    # dataform = LoginForm(request.POST)
     #if dataform.is_valid():
      #   dataform.save()
  
    return render(request, 'pages/about.html', {'lf':LoginForm})

    # we dont need these --- bcz in forms ---  fields = '__all__'  
    # username = request.POST.get('username') #-- value dans forms
    # password = request.POST.get('password')
    #  data = Login(username=username, password=password)
    # date.save()