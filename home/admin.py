from django.contrib import admin
from home.models import Contact, Project, Category

# ✅ Customizing Project admin to display checkbox for categories
class ProjectAdmin(admin.ModelAdmin):
    filter_horizontal = ('categories',)  # This makes categories show as checkboxes

admin.site.register(Contact)
admin.site.register(Category)
admin.site.register(Project, ProjectAdmin)
