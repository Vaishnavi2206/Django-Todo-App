from django.shortcuts import get_object_or_404, render, redirect

from .models import Todo
from .forms import TodoForm
from django.contrib import messages

# Create your views here.

def index(request):
    todos = Todo.objects.all()
    return render(request, 'myapp/tasks.html', {'todos':todos})

# f40227fd-bc4e-4dbf-b7a9-e753e1bd22f9
def create(request):
    print("inside create")
    form = TodoForm(request.POST or None)
    print("method", request.method,form.is_valid())
    if request.method == "POST":
        print("method", form.is_valid())
        if form.is_valid():
            form.save()
            print("form saved")
            messages.success(request, 'Todo created successfully!')
            print("redirecting")
            return redirect('/')
        else:
            messages.error(request, 'Incorrect data. Please check the form fields.')

    return render(request, "myapp/form.html", {"form": form, 'action':'create'})

def edit(request,pk=None):
    print("inside edit")
    todo = get_object_or_404(Todo, pk=pk)
    form = TodoForm(request.POST or None, instance=todo)
    print("todo", todo, request.method)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            print("form saved")
            messages.success(request, 'Feedback updated successfully!')
            print("redirecting")
            return redirect('/')
        else:
            messages.error(request, 'Incorrect data. Please check the form fields.')

    return render(request, "myapp/form.html", {"form": form, 'action':'edit'})

def delete(request, pk=None):
    todo = get_object_or_404(Todo, id=pk)
    todo.delete()
    messages.success(request, 'Feedback deleted successfully!')
    return redirect('/')