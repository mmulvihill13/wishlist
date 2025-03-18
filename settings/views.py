from django.shortcuts import render

from django.contrib.auth.decorators import login_required

@login_required
def setting(request):
    return render(request, "settings/settings.html")  # Ensure this template exists in home/templates/home/


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from .forms import UserUpdateForm  
@login_required
def update_user(request):
    if request.method == "POST":
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, request.user) 
            messages.success(request, "Your profile has been updated successfully!")
            return redirect("settings:setting") 
    else:
        form = UserUpdateForm(instance=request.user)

    return render(request, "settings/update_user.html", {"form": form})

@login_required
def account_page(request):
    return render(request, "settings/account.html")