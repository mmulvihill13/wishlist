from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


# only  want to show home page when user is logged in
# protects view using login_required decorator
# redirects to login page if not logged in
# goes to home if they are

# Create your views here.
def authView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("login:login")
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})