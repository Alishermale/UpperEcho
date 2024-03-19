from django.db import models


class TextData(models.Model):
    text = models.TextField()
