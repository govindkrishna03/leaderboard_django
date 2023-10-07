from django.db import models

# Create your models here.

class Score(models.Model):
    name = models.CharField(max_length=100)
    score = models.IntegerField()

class GitHubCommit(models.Model):
    contributor_name = models.CharField(max_length=100)
    commit_hash = models.CharField(max_length=100)
    commit_message = models.TextField()
    commit_date = models.DateTimeField()

    def __str__(self):
        return f"{self.contributor_name} - {self.commit_hash}"