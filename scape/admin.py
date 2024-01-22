from django.contrib import admin
from .models import Scape, Profile

# Register your models here.
class ScapeAdmin(admin.ModelAdmin):
    list_display = ("name", "owner", "size", "volume", "filtration", "lighting", "co2", "soil")

class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user_profile", "country")

admin.site.register(Scape, ScapeAdmin)
admin.site.register(Profile, ProfileAdmin)