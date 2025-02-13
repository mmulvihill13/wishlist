from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, "home/home.html")  # Ensure this template exists in home/templates/home/
