from django.shortcuts import render, redirect
from .models import Review
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        rating = request.POST.get('rating')
        if content and rating:
            Review.objects.create(
                user=request.user,
                content=content,
                rating=rating
            )

        return redirect('home:home')
    recent_reviews = Review.objects.order_by('-created_at')[:3]
    return render(request, 'home/home.html', {
        'recent_reviews': recent_reviews
    })

def all_reviews(request):
    all_reviews = Review.objects.all().order_by('-created_at')
    
    return render(request, 'home/all_reviews.html', {
        'all_reviews': all_reviews
    })
