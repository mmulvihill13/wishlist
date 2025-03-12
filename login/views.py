from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm


# only  want to show home page when user is logged in
# protects view using login_required decorator
# redirects to login page if not logged in
# goes to home if they are

# Create your views here.
def authView(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST) #or None was here 
        if form.is_valid():
            print("Form is valid")
            user = form.save(commit=False)
            user.email = form.cleaned_data.get("email")
            user.first_name = form.cleaned_data.get("first_name")
            user.last_name = form.cleaned_data.get("last_name")
            user.save()
            return redirect("login:login")
    else:
        form = CustomUserCreationForm()
    return render(request, "registration/signup.html", {"form": form})