from django.contrib import admin
from .models import UserProfile, SecurityAnswer, SecurityQuestion


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'city', 'country', 'profileImage', 'eventInterested')
    search_fields = ('user__username', 'city', 'country')
    list_filter = ('city', 'country')


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(SecurityAnswer)
admin.site.register(SecurityQuestion)
