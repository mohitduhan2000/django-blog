from django.contrib import admin
from .models import About

# admin.site.register(About)

# @admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'updated_at')

    def has_add_permission(self, request):
        count = About.objects.all().count()
        if count == 0:
            return True
        else:
            return False

admin.site.register(About, AboutAdmin)        
