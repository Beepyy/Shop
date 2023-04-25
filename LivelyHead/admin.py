from django.contrib import admin
from .models import *
#admin.site.register(Good)
#admin.site.register(GoodCategory)
admin.site.register(Order)

class GoodCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(GoodCategory, GoodCategoryAdmin)

class GoodAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Good, GoodAdmin)