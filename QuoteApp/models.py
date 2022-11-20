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

class IpLocation(models.Model):
    ip = models.CharField(max_length=225)
    city = models.CharField(max_length=225)
    region = models.CharField(max_length=225)
    country = models.CharField(max_length=225)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"{self.country} | {self.city}"