from django.db import models


class Tag(models.Model):
    nombre = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre
