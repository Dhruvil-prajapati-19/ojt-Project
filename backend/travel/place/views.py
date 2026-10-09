from django.shortcuts import render , redirect
from place.models import *

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('upass')
        print(username)
        print(password)
        dhruvil = register.objects.create(username=username,password=password)
    dhruvil = register.objects.all()
    contacts = {'login': dhruvil}
             
    return render(request,"login.html",contacts)
    # return render(request,"login.html")

def delete(request,id):
    idel = register.objects.get(id=id)
    idel.delete()
    return redirect("login/") 

def update(request,id):
    up = register.objects.get(id=id)
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('upass')
        print(username)
        print(password)
        up = register.objects.filter(id=id).update(username=username,password=password)
        up.save()
        return redirect('login/')
    up = register.objects.all()
    contacts = {'login':up}
    return render(request,'update.html',contacts)


# def home(request):
#     return render(request,'home.html')

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def destination(request):
    return render(request,'destination.html')

