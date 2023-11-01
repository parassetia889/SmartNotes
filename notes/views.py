from django.shortcuts import render
from django.http import Http404
from .models import Notes
from django.views.generic import ListView


class NotesListView(ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_list.html"


def detail(request, pk):
    try:
        note = Notes.objects.get(pk=pk)
        return render(request, "notes/notes_detail.html", {"note": note})
    except Notes.DoesNotExist:
        raise Http404("Note doesn't exist")
