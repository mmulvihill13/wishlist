from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Review  # Import the Review model

@login_required
def home(request):
    recent_reviews = Review.objects.order_by('-created_at')[:3]
    return render(request, "home/home.html", {'recent_reviews': recent_reviews})

def account_view(request):
    return render(request, 'home/account.html')

def all_reviews(request):
    reviews = Review.objects.all()
    return render(request, 'home/all_reviews.html', {'reviews': reviews})
