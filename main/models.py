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
    

class Experience(models.Model):
    job_title = models.CharField(max_length=100, blank=False)
    company_name = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    is_current = models.BooleanField(default=False)
    description = models.TextField()
    technologies = models.CharField(max_length=200, help_text="Comma-separated list of technologies")
    company_logo = models.ImageField(upload_to='company_logos/', null=True, blank=True)
    company_website = models.URLField(default="#", null=True, blank=True)

    def save(self, *args, **kwargs):
        self.technologies = ', '.join([tech.strip() for tech in self.technologies.split(',') if tech.strip()])
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.job_title} at {self.company_name}"