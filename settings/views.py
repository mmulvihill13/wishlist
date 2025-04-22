from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from .forms import UserUpdateForm

@login_required
def setting(request):
    return render(request, "settings/settings.html")

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

@login_required
def delivery_locations(request):
    locations = [
        {
            "name": "Becker",
            "image_url": "https://www.flsouthern.edu/getattachment/aea0efab-b4c7-41d6-9f60-2fd96c21c1f3/fs-2x-bldg-becker.jpg",
            "estimated_delivery_time": "10 minutes"
        },
        {
            "name": "Cafe",
            "image_url": "https://i.pinimg.com/736x/a2/bc/9d/a2bc9d4d9afd8dd98f65e30d349bfee4.jpg",
            "estimated_delivery_time": "20 minutes"
        },
        {
            "name": "Library",
            "image_url": "https://www.travelandleisure.com/thmb/gpiEE4EBnn58CFGRqkZoVwzwS4I=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/florida-southern-university-lakeland-COLLEGECAMP0421-94a6a2c98f5e4a91b86cbe2a7ca134f6.jpg",
            "estimated_delivery_time": "30 minutes"
        },
    ]
    return render(request, "settings/delivery_locations.html", {"locations": locations})
