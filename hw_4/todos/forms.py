from django import forms
from .models import TodoList, Todo

class TodoListForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = ['title', 'description']
        widjets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
        }

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'due_date', 'status']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'due_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'status': forms.CheckboxInput(attrs={'class': 'form-ccheck-input'}),
        }