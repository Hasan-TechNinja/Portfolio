from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return f"Message from {self.email}"

class Footer(models.Model):
    title = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='footer')
    url = models.URLField(default='#')

    def __str__(self):
        return f"{self.title} logo"