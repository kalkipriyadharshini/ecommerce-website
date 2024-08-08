from django.shortcuts import render,redirect
from django.http import HttpResponse 
from django.template import loader
from .models import Datas
from django.contrib import messages
from django.contrib.auth import login, authenticate
from.forms import UserRegistrationForm

# Create your views here.
def frame(request):
    template = loader.get_template('frame.html')
    return HttpResponse(template.render())

def home(request): # 127.0.0.1:8000/
  mydata=Datas.objects.all()
  if(mydata!=""):
    return render(request,"home.html",{"datas":mydata})
  else:
    return render(request,"home.html")  
  
def addData(request):
  if request.method=="POST":
    name=request.POST["name"]
    age=request.POST["age"]
    Contect=request.POST["Contect"]
    address=request.POST["address"]
    mail=request.POST["mail"]
    
    obj=Datas()
    obj.Name=name
    obj.Age=age
    obj.Contect=Contect
    obj.Address=address
    obj.Mail=mail
    obj.save()
    mydata=Datas.objects.all()
    return redirect("home")
  return render(request,"home.html")

def updateData(request,id):
  mydata=Datas.objects.get(id=id)
  if request.method=="POST":
    name=request.POST["name"]
    age=request.POST["age"]
    contect=request.POST["contect"]
    address=request.POST["address"]
    mail=request.POST["mail"]
    
    mydata.Name=name
    mydata.Age=age
    mydata.Contect=contect
    mydata.Address=address
    mydata.Mail=mail
    mydata.save()
    return redirect("home")
  return render(request,"update.html",{"data":mydata})

def deleteData(request,id):
  mydata=Datas.objects.get(id=id)
  mydata.delete()
  return redirect("home")


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created. You can log in now!')
            return redirect('login')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'register.html', context)

def home1(request):
  template = loader.get_template('home1.html')
  return HttpResponse(template.render())

def login(request):
  template = loader.get_template('login.html')
  return HttpResponse(template.render())
	

def logout(request):
  template = loader.get_template('logout.html')
  return HttpResponse(template.render())
	