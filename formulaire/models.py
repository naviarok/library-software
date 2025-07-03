from django.db import models

# Create your models here.
class Formulaire(models.Model):
    FirstName = models.CharField(max_length=100, null=True, blank=True)
    LastName = models.CharField(max_length=100, null=True, blank=True)
    Fillier = models.CharField(max_length=100, null=True, blank=True)
    Code = models.CharField(max_length=100, null=True, blank=True)
    Items = models.CharField(max_length=200, null=True, blank=True)
    Date = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self) -> str:
        return str(f"{self.FirstName}")