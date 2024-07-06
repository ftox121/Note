from django.urls import path
from notesapp.views import notes_view, delete_note_view

urlpatterns = [
    path('', notes_view, name='notes_view'),
    path('delete_note/<int:note_id>/', delete_note_view, name='delete_note'),
]
