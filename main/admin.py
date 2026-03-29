from django.contrib import admin
from .models import Contact, SocialLink, Experience, About, SkillImage, Projects


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'short_message', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'email', 'message')
    readonly_fields = ('name', 'email', 'message', 'created_at')

    def short_message(self, obj):
        return obj.message[:80] + '...' if len(obj.message) > 80 else obj.message
    short_message.short_description = 'Message'

    def has_add_permission(self, request):
        return False


@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'url', 'order', 'status')
    list_editable = ('order', 'status')
    actions = ["enable", "disable"]

    @admin.action(description="Enable selected")
    def enable(self, request, queryset):
        queryset.update(status=True)

    @admin.action(description="Disable selected")
    def disable(self, request, queryset):
        queryset.update(status=False)


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('id', 'job_title', 'company_name', 'location', 'start_date', 'end_date', 'is_current', 'status')
    list_filter = ('status', 'is_current')
    list_editable = ('status',)
    actions = ["enable", "disable"]

    @admin.action(description="Enable selected")
    def enable(self, request, queryset):
        queryset.update(status=True)

    @admin.action(description="Disable selected")
    def disable(self, request, queryset):
        queryset.update(status=False)


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'role', 'email', 'phone', 'status')
    list_editable = ('status',)
    actions = ["enable", "disable"]

    @admin.action(description="Enable selected")
    def enable(self, request, queryset):
        queryset.update(status=True)

    @admin.action(description="Disable selected")
    def disable(self, request, queryset):
        queryset.update(status=False)


@admin.register(SkillImage)
class SkillImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'order', 'status')
    list_filter = ('category', 'status')
    list_editable = ('order', 'status', 'category')
    actions = ["enable", "disable"]

    @admin.action(description="Enable selected")
    def enable(self, request, queryset):
        queryset.update(status=True)

    @admin.action(description="Disable selected")
    def disable(self, request, queryset):
        queryset.update(status=False)


@admin.register(Projects)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'order', 'status')
    list_filter = ('category', 'status')
    list_editable = ('order', 'status')
    search_fields = ('name', 'category', 'description')
    actions = ["enable", "disable"]

    @admin.action(description="Enable selected")
    def enable(self, request, queryset):
        queryset.update(status=True)

    @admin.action(description="Disable selected")
    def disable(self, request, queryset):
        queryset.update(status=False)