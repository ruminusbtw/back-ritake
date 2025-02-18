from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_list_or_404, redirect, get_object_or_404
from .models import TodoList, Todo
from .forms import TodoListForm, TodoForm

def redirect_to_todos_lists(request):
    return redirect('todo_list')

def todo_list_view(request):
    todo_lists = TodoList.objects.all()
    form = TodoListForm()
    return render(request, 'todos/todo_list.html', {'todo_lists': todo_lists, 'form': form})

def todo_list_detail(request, id):
    todo_list = get_list_or_404(TodoList, id=id)
    todos = Todo.objects.filter(todo_list=todo_list)
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.todo_list = todo_list
            todo.save()
            return redirect('todo_list_detail', id=id)
    else:
        form = TodoForm()
    return render(request, 'todos/todo_list_detail.html', {'todo_list': todo_list, 'todos': todos, 'form': form})

def todo_list_edit(request, id):
    todo_list = get_list_or_404(TodoList, id=id)
    if request.method == 'POST':
        form = TodoListForm(request.POST, instance=todo_list)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoListForm(instance=todo_list)
    return render(request, 'todos/todo_list_edit.html', {'form': form})

def todo_list_delete(request, id):
    todo_list = get_list_or_404(TodoList, id=id)
    todo_list.delete()
    return redirect('todo_list')

def todo_edit(request, id):
    todo = get_list_or_404(Todo, id=id)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo_list_detail', id=todo.todo_list.id)
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todos/todo_edit.html', {'form': form})

def todo_delete(request, id):
    todo = get_list_or_404(Todo, id=id)
    todo_list_id = todo.todo_list.id
    todo.delete()
    return redirect('todo_list_detail', id=todo_list_id)

def todo_create(request):
    if request.method == 'POST':
        todo_list_id = request.POST.get('todo_list')
        todo_list = get_object_or_404(TodoList, id=todo_list_id)

        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.todo_list = todo_list
            todo.save()
            return redirect('todo_list_detail', id=todo_list.id)
    else:
        form = TodoForm()

    return render(request, 'todos/todo_create.html', {'form': form})