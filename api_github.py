import requests
from django.conf import settings

def fetch_github_commits(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"

    headers = {
        "Authorization": f"Bearer {settings.GITHUB_API_KEY}"
    }

    response = requests.get(url, headers=headers)

    owner_name = ["govindkrishna03", "Govind Krishna", "Wreck-X", "Viserion-7", "Ivin J. Abraham"]

    if response.status_code == 200:
        commits = response.json()

        commit_count = {}

        for commit in commits:
            contributor_name = commit['commit']['author']['name']

            if contributor_name not in owner_name:
                commit_count[contributor_name] = commit_count.get(contributor_name, 0) + 1

        ranked_contributors = sorted(commit_count.items(), key=lambda x: x[1], reverse=True)

        return ranked_contributors

    else:
        raise Exception(f"Failed to fetch GitHub commits: {response.status_code}")
