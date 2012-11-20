from django.contrib.gis import admin
from gameon.submissions import models


class ChallengeAdmin(admin.ModelAdmin):
    model = models.Challenge
    prepopulated_fields = {"slug": ("name",)}


class CategoryAdmin(admin.ModelAdmin):
    model = models.Category
    prepopulated_fields = {"slug": ("name",)}


class EntryAdmin(admin.ModelAdmin):
    model = models.Entry
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(models.Challenge, ChallengeAdmin)
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Entry, EntryAdmin)
