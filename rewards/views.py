from django.shortcuts import render

def reward(request):
    return render(request, "rewards/rewards.html")  # Ensure this template exists in home/templates/home/
