from django.shortcuts import render

from django.contrib.auth.decorators import login_required

def setting(request):
    return render(request, "settings/settings.html")  # Ensure this template exists in home/templates/home/



@login_required
def account_page(request):
    return render(request, 'account.html', {'user': request.user})
