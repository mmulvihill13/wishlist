from django.contrib import admin

# Register your models here.python manage.py makemigrations
from .models import Announcement

from .models import Review

admin.site.register(Review)

@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'content')


