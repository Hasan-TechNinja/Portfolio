from django.db import models
from datetime import date


class Contact(models.Model):
    name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Message from {self.email}"


class SocialLink(models.Model):
    title = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='footer', blank=True, null=True)
    url = models.URLField(default='#')
    order = models.PositiveIntegerField(default=0, help_text="Display order (lower = first)")
    status = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

    @property
    def get_logo_url(self):
        if self.logo:
            return self.logo.url
            
        title_lower = self.title.lower()
        url_lower = self.url.lower()
        from django.templatetags.static import static
        
        # Check common networks for local static images
        if 'facebook' in title_lower or 'facebook.com' in url_lower:
            return static('image/facebook.png')
        elif 'linkedin' in title_lower or 'linkedin.com' in url_lower:
            return static('image/linkedin.png')
        elif 'github' in title_lower or 'github.com' in url_lower:
            return static('image/github.png')
        elif 'instagram' in title_lower or 'instagram.com' in url_lower:
            return static('image/instagram.png')
        elif 'whatsapp' in title_lower or 'wa.me' in url_lower:
            return static('image/whatsapp.png')
        elif 'twitter' in title_lower or 'twitter.com' in url_lower or 'x.com' in url_lower:
            return static('image/portfolio.png') # Fallback
            
        # Fallback to Google Favicon
        from urllib.parse import urlparse
        try:
            domain = urlparse(self.url).netloc
            if domain:
                return f"https://www.google.com/s2/favicons?domain={domain}&sz=64"
        except Exception:
            pass
            
        # Generic globe fallback
        return static('image/portfolio.png')


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
    status = models.BooleanField(default=True)

    class Meta:
        ordering = ['-start_date']

    def save(self, *args, **kwargs):
        self.technologies = ', '.join([tech.strip() for tech in self.technologies.split(',') if tech.strip()])
        super().save(*args, **kwargs)

    def calculate_experience(self):
        end_date = self.end_date if self.end_date else date.today()
        duration = end_date - self.start_date
        return duration.days

    @property
    def duration_display(self):
        """Smart duration: <1 month → days, <1 year → months, else → years + months."""
        end = self.end_date if self.end_date else date.today()
        # Calculate years and months using calendar math
        total_months = (end.year - self.start_date.year) * 12 + (end.month - self.start_date.month)
        if end.day < self.start_date.day:
            total_months -= 1

        if total_months < 1:
            # Less than 1 month — show days
            days = (end - self.start_date).days
            if days == 0:
                return "Just started"
            elif days == 1:
                return "1 day"
            else:
                return f"{days} days"
        elif total_months < 12:
            # Less than 1 year — show months
            if total_months == 1:
                return "1 month"
            else:
                return f"{total_months} months"
        else:
            # 1+ years — show years and months
            years = total_months // 12
            months = total_months % 12
            parts = []
            parts.append(f"{years} year{'s' if years > 1 else ''}")
            if months > 0:
                parts.append(f"{months} month{'s' if months > 1 else ''}")
            return " ".join(parts)

    def __str__(self):
        return f"{self.job_title} at {self.company_name}"

    @property
    def technologies_list(self):
        """Return technologies as a list for template rendering."""
        if self.technologies:
            return [tech.strip() for tech in self.technologies.split(',') if tech.strip()]
        return []


class About(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    role = models.CharField(max_length=200, default="Full Stack Developer", help_text="e.g. Full Stack Developer, Backend Engineer")
    email = models.EmailField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    education = models.CharField(max_length=400)
    description = models.TextField()
    CV = models.FileField(upload_to='cv')
    image = models.ImageField(upload_to='profile')
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


SKILL_CATEGORIES = [
    ('language', 'Languages'),
    ('framework', 'Frameworks'),
    ('tool', 'Tools & Platforms'),
    ('database', 'Databases'),
    ('devops', 'Cloud & DevOps'),
    ('other', 'Other'),
]


class SkillImage(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='skill')
    category = models.CharField(max_length=20, choices=SKILL_CATEGORIES, default='other')
    order = models.PositiveIntegerField(default=0, help_text="Display order (lower = first)")
    status = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name


PROJECT_CATEGORIES = [
    # General Web/Tech
    ('portfolio', 'Portfolio'),
    ('blog', 'Blog'),
    ('saas', 'SaaS'),
    ('ai-ml', 'AI / ML'),

    # Mobile & App Store Categories
    ('art-design', 'Art & Design'),
    ('business', 'Business'),
    ('communication', 'Communication'),
    ('dating', 'Dating'),
    ('education', 'Education'),
    ('entertainment', 'Entertainment'),
    ('finance', 'Finance'),
    ('food-drink', 'Food & Drink'),
    ('games', 'Games'),
    ('health-fitness', 'Health & Fitness'),
    ('kids', 'Kids'),
    ('lifestyle', 'Lifestyle'),
    ('medical', 'Medical'),
    ('music-audio', 'Music & Audio'),
    ('navigation', 'Maps & Navigation'),
    ('news', 'News & Magazines'),
    ('photo-video', 'Photo & Video'),
    ('productivity', 'Productivity'),
    ('shopping', 'Shopping / E-commerce'),
    ('social', 'Social Networking'),
    ('sports', 'Sports'),
    ('tools', 'Tools & Utilities'),
    ('travel', 'Travel & Local'),
    ('weather', 'Weather'),
    
    ('other', 'Other'),
]


class Projects(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=PROJECT_CATEGORIES, default='other')
    start = models.DateField(blank=True, null=True)
    end = models.DateField(blank=True, null=True)
    description = models.TextField()
    image = models.ImageField(upload_to='projects')
    github = models.CharField(max_length=500, blank=True, null=True)
    live = models.CharField(max_length=500, blank=True, null=True)
    order = models.PositiveIntegerField(default=0, help_text="Display order (lower = first)")
    status = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']
        verbose_name_plural = "Projects"

    def project_duration(self):
        if self.start and self.end:
            return (self.end - self.start).days
        return None

    def is_ongoing(self):
        return self.end is None

    def __str__(self):
        return self.name
