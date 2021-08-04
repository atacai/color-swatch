from django.contrib import admin
from .models        import Color, Range


class RangeInLine(admin.TabularInline):
    model = Range
    extra = 0


class ColorAdmin(admin.ModelAdmin):
    inlines = (RangeInLine,)


admin.site.register(Color, ColorAdmin)
