from django.shortcuts import render,redirect
from . import forms
from .models import list
from django.contrib import messages

def home(request):
    if request.method == 'POST':
        form = forms.listform(request.POST or None)
        if form.is_valid():
            form.save()
            all_items = list.objects.all()
            messages.success(request, 'Item has been added successfully to the list')
            return render(request, 'todo_list/home.html', {'items':all_items})   
    else:
        all_items = list.objects.all()
        return render(request, 'todo_list/home.html', {'items':all_items})
    
def del_event(request, event_id):
    listevent = list.objects.get(pk=event_id)
    listevent.delete()
    messages.success(request, 'Item has been deleted successfully from the list')
    return redirect('home')

def cross_off(request, id):
    item = list.objects.get(pk=id)
    item.completed = True
    item.save()
    return redirect('home')


def uncross(request, id):
    item = list.objects.get(pk=id)
    item.completed = False
    item.save()
    return redirect('home')

def about(request):
        return render(request, 'todo_list/about.html',{})    


