# Create your models here.
from django.db import models
from django.contrib.auth import get_user_model

class Template(models.Model):
    """Table Django des templates comme demandé dans les consignes"""
    nom = models.CharField(max_length=255)
    desc = models.TextField(help_text="La description")
    createur = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    html= models.TextField(help_text="Code HTML du template qu'on va proposer à remplir ")
    json = models.JSONField(help_text="Code JSON du template qu'on va proposer à remplir ")



