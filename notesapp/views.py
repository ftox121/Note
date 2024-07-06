from django.shortcuts import render, redirect, get_object_or_404
from notesapp.models import Notes
from notesapp.forms import NoteForm

def notes_view(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notes_view')
    else:
        form = NoteForm()

    notes = Notes.objects.all()
    return render(request, 'notesapp/note.html', {'form': form, 'notes': notes})

def delete_note_view(request, note_id):
    note = get_object_or_404(Notes, id=note_id)
    if request.method == 'POST':
        note.delete()
        return redirect('notes_view')
    return redirect('notes_view')
