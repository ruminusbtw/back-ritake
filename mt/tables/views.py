from django.shortcuts import render, redirect, get_object_or_404
from .models import Table
from .forms import TableForm

def table_list(request):
    tables = Table.objects.all()
    return render(request, 'tables/list.html', {'tables': tables})

def available_tables(request):
    tables = Table.objects.filter(is_available=True)
    return render(request, 'tables/available.html', {'tables': tables})

def add_table(request):
    if request.method == "POST":
        form = TableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("table_list") 
    else:
        form = TableForm()

    return render(request, "tables/add_table.html", {"form": form})