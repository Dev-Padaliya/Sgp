from django.shortcuts import render, redirect
from django.contrib.auth import logout

from item.models import Category, Item
from .forms import SignupFrom

def index(request):
    items = Item.objects.filter(is_donated=False)[0:6]
    categories= Category.objects.all()
    return render(request,'core/index.html', {
        'categories': categories,
        'items': items
    })

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form= SignupFrom(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    
    else:
        form= SignupFrom()
    

    return render(request, 'core/signup.html',{
        'form': form
    })

def logout_view(request):
    logout(request)
    items = Item.objects.filter(is_donated=False)[0:6]
    categories= Category.objects.all()
    return render(request,'core/index.html', {
        'categories': categories,
        'items': items
    })