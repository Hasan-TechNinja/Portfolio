from django.contrib import admin
from .models import Contact, Footer

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'message')
    
admin.site.register(Contact, ContactAdmin)


class FooterAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'logo', 'url')

admin.site.register(Footer, FooterAdmin)