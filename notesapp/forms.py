from django.forms import ModelForm
from notesapp.models import *

class NoteForm(ModelForm):
    class Meta:
        model = Notes
        fields = '__all__'
