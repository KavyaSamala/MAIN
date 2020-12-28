from django.contrib import admin
from .models import MasterPackage, Package, Version

admin.site.register(MasterPackage)
admin.site.register(Package)
admin.site.register(Version)