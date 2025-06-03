from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from home import views

# Admin branding
admin.site.site_header = "Login to Burhan"
admin.site.site_title = "Welcome to Dashboard"
admin.site.index_title = "Welcome to Portal"

urlpatterns = [
    path('admin/', admin.site.urls),  # ✅ Added admin route
    path('', views.home, name='home'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
]

# ✅ Serve static and media files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
