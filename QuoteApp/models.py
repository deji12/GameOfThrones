from django.db import models

class Actor(models.Model):
    quoter = models.CharField(max_length=225, null=True, blank=True)

    def __str__(self):
        return self.quoter

class Quote(models.Model):
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE, null=True, blank=True)
    quote = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return f"{self.actor} | {self.quote}"
