from django.contrib import admin
from .models        import ColorSpace, Range


class RangeInLine(admin.TabularInline):
    model = Range
    extra = 0


class ColorSpaceAdmin(admin.ModelAdmin):
    inlines = (RangeInLine,)


admin.site.register(ColorSpace, ColorSpaceAdmin)
