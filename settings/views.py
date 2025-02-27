from django.shortcuts import render

def setting(request):
    return render(request, "settings/settings.html")  # Ensure this template exists in home/templates/home/
