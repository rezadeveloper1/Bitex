from django.db import models

class KeyValueModel(models.Model):
    key = models.CharField(max_length=100)
    value = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.key} - {self.value}"
    