from django.shortcuts import render, redirect, get_object_or_404      
from .forms import NoteModelForm
from django.views.generic.list import ListView

# Create your views here.
from .models import Note


def create_view(request):

    form = NoteModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.instance.user = request.user
        form.save()
        return redirect('/')

    context = {
        'form': form
    }

    return render(request, "notepad/base.html", context)

def home_view(request):
    form = NoteModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.instance.user = request.user
        form.save()
        return redirect('/')

    context = {
        'form': form
    }
    return render(request, "notepad/base.html", context)
    
class NoteList(ListView):
    model = Note
    context_object_name = 'object_list'
    template_name = "notepad/list.html"

def delete_view(request, id):
    item_to_delete = Note.objects.filter(pk=id)
    if item_to_delete.exists():
        if request.user == item_to_delete[0].user:
            item_to_delete[0].delete()
    return redirect('/list')

def update_view(request, id):
    unique_note = get_object_or_404(Note, id=id)
    form = NoteModelForm(request.POST or None, request.FILES or None, instance=unique_note)
    if form.is_valid():
        form.instance.user = request.user
        form.save()
        return redirect('/list')

    context = {
        'form': form
    }
    return render(request, "notepad/update.html", context)

