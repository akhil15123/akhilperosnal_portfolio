from django.contrib import admin
from home.models import Contact, Project  # ✅ updated model name

admin.site.register(Contact)
admin.site.register(Project)  # ✅ register the unified dynamic project model
