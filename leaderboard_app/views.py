from django.shortcuts import render
from .models import Score


def leaderboard_view(request):
    scores = Score.objects.all().order_by("-score")[:10]
    return render(request, "leaderboard/leaderboard.html", {"scores": scores})