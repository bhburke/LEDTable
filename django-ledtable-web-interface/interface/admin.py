from django.contrib import admin
from interface.models import Animation, Option


class OptionInline(admin.TabularInline):
    model = Option
    extra = 2


class AnimationAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
    ]
    inlines = [OptionInline]

admin.site.register(Animation, AnimationAdmin)