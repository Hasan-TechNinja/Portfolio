from django.contrib import admin
from .models import Contact, Footer, Experience, About, Skill, SkillImage, Projects

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'message')
    # actions = ["Enable", "Disable"]

    # @admin.action(description="Enable")
    # def Enable(self, request, status):
    #     status.update(status = "True")

    # @admin.action(description="Disable")
    # def Disable(self, request, status):
    #     status.update(status = "False")
    
admin.site.register(Contact, ContactAdmin)


class FooterAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'logo', 'url', 'status')
    actions = ["Enable", "Disable"]

    @admin.action(description="Enable")
    def Enable(self, request, status):
        status.update(status = "True")

    @admin.action(description="Disable")
    def Disable(self, request, status):
        status.update(status = "False")

admin.site.register(Footer, FooterAdmin)

class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('id', 'job_title', 'company_name', 'location', 'start_date', 'end_date', 'is_current', 'description', 'technologies', 'company_logo', 'company_website', 'status')
    actions = ["Enable", "Disable"]

    @admin.action(description="Enable")
    def Enable(self, request, status):
        status.update(status = "True")

    @admin.action(description="Disable")
    def Disable(self, request, status):
        status.update(status = "False")

admin.site.register(Experience, ExperienceAdmin)

class AboutAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'phone', 'education', 'description', 'CV', 'image', 'status')
    actions = ["Enable", "Disable"]

    @admin.action(description="Enable")
    def Enable(self, request, status):
        status.update(status = "True")

    @admin.action(description="Disable")
    def Disable(self, request, status):
        status.update(status = "False")

admin.site.register(About, AboutAdmin)


class SkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'programming_languages', 'frameworks', 'tolse_and_platforms', 'databases', 'cloud_and_devops', 'soft_skills', 'operating_systems', 'version_control', 'testing', 'others', 'status')
    actions = ["Enable", "Disable"]

    @admin.action(description="Enable")
    def Enable(self, request, status):
        status.update(status = "True")

    @admin.action(description="Disable")
    def Disable(self, request, status):
        status.update(status = "False")

admin.site.register(Skill, SkillAdmin)

class SkillImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image', 'status')
    actions = ["Enable", "Disable"]

    @admin.action(description="Enable")
    def Enable(self, request, status):
        status.update(status = "True")

    @admin.action(description="Disable")
    def Disable(self, request, status):
        status.update(status = "False")

admin.site.register(SkillImage, SkillImageAdmin)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'start', 'end', 'description', 'image', 'github', 'live', 'status')
    actions = ["Enable", "Disable"]

    @admin.action(description="Enable")
    def Enable(self, request, status):
        status.update(status = "True")

    @admin.action(description="Disable")
    def Disable(self, request, status):
        status.update(status = "False")

admin.site.register(Projects, ProjectAdmin)