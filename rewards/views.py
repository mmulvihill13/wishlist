from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def reward(request):
    profile = request.user.profile
    drinks_until_free = 10 - (profile.order_count % 10)
    progress_percent = round((1 - (drinks_until_free / 10)) * 100)

    context = {
        'order_count': profile.order_count,
        'free_drinks': profile.free_drinks_avail,
        'drinks_until_free': drinks_until_free if drinks_until_free != 0 else 10,  # in case they just earned one
        'progress_percent': progress_percent,
    }
    return render(request, 'rewards/rewards.html', context)
