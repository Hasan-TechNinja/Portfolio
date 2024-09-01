from django.contrib import admin
from .models import Contact, Footer, Experience

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'message')
    
admin.site.register(Contact, ContactAdmin)


class FooterAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'logo', 'url')

admin.site.register(Footer, FooterAdmin)

class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('id', 'job_title', 'company_name', 'location', 'start_date', 'end_date', 'is_current', 'description', 'technologies', 'company_logo', 'company_website')

admin.site.register(Experience, ExperienceAdmin)