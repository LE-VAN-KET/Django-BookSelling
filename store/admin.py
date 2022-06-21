from django.contrib import admin
from .models import Category, Book, Publisher, Author, BookCategory


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'parent']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class PublisherAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Publisher, PublisherAdmin)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'create_at', 'update_at']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Author, AuthorAdmin)


class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity',
                    'total_review', 'rating', 'state',
                    'author', 'author', 'publisher',
                    'sold_quantity', 'public_year',
                    'language', 'weight', 'discount']

    list_filter = ['state']
    list_editable = ['price', 'quantity', 'state']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Book, BookAdmin)
