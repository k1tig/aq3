from django.contrib import admin
from .models import TankSize, TankVolume, TankFilter, TankLight, TankCo2, TankSoil, TankHardscape

admin.site.register(TankSize)
admin.site.register(TankVolume)
admin.site.register(TankFilter)
admin.site.register(TankLight)
admin.site.register(TankCo2)
admin.site.register(TankSoil)
admin.site.register(TankHardscape)


