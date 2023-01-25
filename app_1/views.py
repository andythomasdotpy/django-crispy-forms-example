from django.shortcuts import render

from .forms import UniversityForm

# Create your views here.

def index(request):
    context = {"form": UniversityForm()}
    return render(request, "app_1/index.html", context)