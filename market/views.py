from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import item,Carts
from .forms import ItemForm
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from datetime import date
from django.contrib import messages

# Create your views here.

def index(request):
    n=item.objects.all()
    return render(request,"market/index.html",{'n':n})

def details(request,pk):
    n=item.objects.get(pk=pk)
    return render(request,"market/item_form.html",{'n':n})
    

def market(request):
    form= ItemForm()
    if request.method=="POST":
        form=ItemForm(request.POST,request.FILES)
        if form.is_valid:
            form.save()
            return redirect('/')
    else:
        form=ItemForm()
    return render(request,"market/marketplace.html",{'form':form})

def delete_cart(request,pk):
    a=Carts.objects.get(pk=pk)
    a.delete()
    n=Carts.objects.filter(author=request.user.username)
    return render(request,'market/checkout.html',{'n':n})

def cart(request,pk):
    m=item.objects.get(pk=pk)
    user=None
    try:
        user = Carts.objects.get(name=m)
    except Carts.DoesNotExist:
        user = None
    if user == None:
        a=Carts.objects.create(author=request.user.username,image=m.img,name=m,date=date.today())
        a.save()
    else:
        return HttpResponse ('already added')
    return render(request,"market/item_form.html",{'m':m})

def checkout(request):
    n=Carts.objects.filter(author=request.user.username)
    return render(request,'market/checkout.html',{'n':n})

def profile(request):
    n=(item.objects.filter(author=request.user.username))
    d={}
    k=0
    for i in n:
        d[i.pk]=(item.objects.get(pk=i.pk))
    print(d)
    return render(request,'market/account.html',{'d':d})

def register(request):
    if(request.method=="POST"):
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
    else:
        form=UserCreationForm()
    return render(request,'market/signup.html',{'form':form})

def search(request):
    name=request.POST.get('name')
    n=None
    try:
        n = item.objects.filter(name__icontains=name)
    except item.DoesNotExist:
        n = None
    if n == None:
        messages.warning(request,'Not Found, Try Again')
    else:
        return render(request,"market/index.html",{'n':n})
    