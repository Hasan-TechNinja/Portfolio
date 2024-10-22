from django.db import models
from datetime import date

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
    company_website = models.CharField(max_length=500, default="#")

    def save(self, *args, **kwargs):
        self.technologies = ', '.join([tech.strip() for tech in self.technologies.split(',') if tech.strip()])
        super().save(*args, **kwargs)

    def calculate_experience(self):
        end_date = self.end_date if self.end_date else date.today()
        duration = end_date - self.start_date
        return duration.days

    def calculate_experience_years(self):
        days = self.calculate_experience()
        years = days // 365
        remaining_days = days % 365
        return years, remaining_days

    def __str__(self):
        return f"{self.job_title} at {self.company_name}"
    

    
class About(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, blank=True, null= True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    education = models.CharField(max_length=400)
    description = models.TextField()
    CV = models.FileField(upload_to='cv')
    image = models.ImageField(upload_to='profile')

def __str__(self):
    return f"{self.first_name} {self.last_name} information"


class Skill(models.Model):
    programming_languages = models.CharField(max_length=500, blank=True, null=True)
    frameworks = models.CharField(max_length=500, blank=True, null=True)
    tolse_and_platforms = models.CharField(max_length=500, blank=True, null=True)
    databases = models.CharField(max_length=500, blank=True, null=True)
    cloud_and_devops = models.CharField(max_length=500, blank=True, null=True)
    soft_skills = models.CharField(max_length=500, blank=True, null=True)
    operating_systems = models.CharField(max_length=500, blank=True, null=True)
    version_control = models.CharField(max_length=500, blank=True, null=True)
    testing = models.CharField(max_length=500, blank=True, null=True)
    others = models.CharField(max_length=900, blank=True, null=True)

    def __str__(self):
        return f"Skills: {self.programming_languages or 'N/A'}, {self.frameworks or 'N/A'}"
    
class SkillImage(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='skill')

    def __str__(self):
        return f"{self.image} logo"
    

class Projects(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200, blank=True, null=True)
    start = models.DateField(blank=True, null=True)
    end = models.DateField(blank=True, null=True)
    description = models.TextField()
    image = models.ImageField(upload_to='projects')
    github = models.CharField(max_length=500, blank=True, null=True)
    live = models.CharField(max_length=500, blank=True, null=True)

    def project_duration(self):
        if self.start and self.end:
            return (self.end - self.start).days
        return None

    def is_ongoing(self):
        return self.end is None

    def __str__(self):
        return self.name
