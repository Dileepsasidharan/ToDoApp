from django.shortcuts import render, redirect

from todoapp.forms import TodoForm
from todoapp.models import todoapp


# Create your views here.
def todo(request):
    return render(request,'index.html')
def addtodo(request):
    return render(request,'addtodo.html')
def addtodo(request):
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect('todo')
    return render(request,"addtodo.html",{'form':form})
def viewtodo(request):
    data=todoapp.objects.all()
    return render(request,'viewtodo.html',{'data':data})
def update_todo(request,id):
    data=todoapp.objects.get(id=id)
    form=TodoForm(instance=data)
    if request.method=='POST':
        form = TodoForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('viewtodo')
    return render(request, "updatetodo.html", {'form': form})
def del_todo(id):
    todoapp.objects.get(id=id).delete()
    return redirect('viewtodo')


