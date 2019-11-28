from django import forms
from django.db import models
from django.urls import reverse

class Post(models.Model):
    texto = models.TextField()
    autor = models.CharField(max_length=50)
    publicacao = models.DateField(auto_now_add=True)

    def __str__(self):
        str = '{0} (de {1})'
        return str.format(self.texto, self.autor)

    def get_absolute_url(self):
        return reverse('main:index')
