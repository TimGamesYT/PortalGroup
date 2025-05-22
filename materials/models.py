from django.db import models

class Material(models.Model):
    description = models.CharField(max_length=100)
    media = models.FileField(upload_to='materials/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description
    
