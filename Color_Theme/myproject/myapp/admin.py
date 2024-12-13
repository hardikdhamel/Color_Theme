from django.contrib import admin
from django.contrib.admin import AdminSite
from django.utils.html import format_html

# Register your models here.

class MyAdminSite(AdminSite):
    site_header = "My Custom Admin"
    site_title = "My Admin Dashboard"
    
    def get_urls(self):
        urls = super().get_urls()
        return urls

    class Media:
        css = {
            'all': ('myapp/css/custom_admin.css',)
        }

admin.site = MyAdminSite()