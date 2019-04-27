from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('notes/',views.notes, name='notes'),
    path('addnotes/',views.uploadnotes, name='addnotes')
    path('notes/',views.deletenotes, name='deletenotes')
]
