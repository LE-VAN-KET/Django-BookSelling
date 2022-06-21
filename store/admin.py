from django.contrib import admin
from .models import Category, Writer, Book, Slider


class AdminCategory(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, AdminCategory)


class AdminWriter(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Writer, AdminWriter)


class AdminBook(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'status', 'created', 'updated']
    list_filter = ['status', 'created', 'updated']
    list_editable = ['price', 'stock', 'status']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Book, AdminBook)


class AdminSlider(admin.ModelAdmin):
    list_display = ['title', 'created', 'updated']


admin.site.register(Slider, AdminSlider)
