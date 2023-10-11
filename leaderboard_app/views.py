from django.shortcuts import render
from api_github import fetch_github_commits 
def leaderboard_view(request):
    owner = 'Govind Krishna'
    repo = 'Hacktober_2023'

    commits = fetch_github_commits(owner, repo)
    
    context = {'ranked_contributors': commits} 
    return render(request, "leaderboard/leaderboard.html", context)
