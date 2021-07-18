from django.contrib import admin
from .models import Message, Profile


class MessageAdmin(admin.ModelAdmin):
    list_display = (
        'sender',
        'message'
    )
    list_filter = (
        'sender',
    )
    search_fields = [
        'message'
    ]
    readonly_fields = (
        'sender',
        'receiver',
        'message'
    )
    actions_on_bottom = False
    actions_on_top = True
admin.site.register(Message, MessageAdmin)

# register profile model to admin as class ProfileAdmin
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo']
admin.site.register(Profile, ProfileAdmin)
