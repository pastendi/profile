from django.contrib import admin
from .models import Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "desc", "website", "github")


admin.site.register(Project, ProjectAdmin)