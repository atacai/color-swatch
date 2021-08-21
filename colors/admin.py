from django.contrib import admin
from .models        import ColorSpace, Attribute


class AttributeInLine(admin.TabularInline):
    model = Attribute
    extra = 0


class ColorSpaceAdmin(admin.ModelAdmin):
    inlines = (AttributeInLine,)


admin.site.register(ColorSpace, ColorSpaceAdmin)
