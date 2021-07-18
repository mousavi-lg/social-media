from django.contrib import admin
from .models import Profile

# register profile model to admin as class ProfileAdmin
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo']
admin.site.register(Profile, ProfileAdmin)
