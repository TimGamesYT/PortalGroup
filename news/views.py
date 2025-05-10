from django.shortcuts import render
from django.views.generic import ListView
from .models import Novation, Announ

class NovationsListView(ListView):
    model = Novation
    context_object_name = "novations"

class AnnounsListView(ListView):
    model = Announ
    context_object_name = "announs"
