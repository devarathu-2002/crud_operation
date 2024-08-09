# myapp/views.py
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login
from .models import Item
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('crud')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')
@login_required
def crud_view(request):
    items = Item.objects.all()
    return render(request, 'crud.html', {'items': items})

@login_required
def create_item(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        Item.objects.create(name=name, description=description)
        return redirect('crud')
    return render(request, 'create_item.html')

@login_required
def update_item(request, id):
    item = get_object_or_404(Item, id=id)
    if request.method == 'POST':
        item.name = request.POST['name']
        item.description = request.POST['description']
        item.save()
        return redirect('crud')
    return render(request, 'update_item.html', {'item': item})

@login_required
def delete_item(request, id):
    item = get_object_or_404(Item, id=id)
    if request.method == 'POST':
        item.delete()
        return redirect('crud')
    return render(request, 'delete_item.html', {'item': item})