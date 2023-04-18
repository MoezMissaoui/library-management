from django.contrib import admin
from .models import Book, BookInstance

# Register your models here.

class BooksInstanceInline(admin.TabularInline):
    model = BookInstance


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'book', 'status', 'borrower', 'due_back', 'is_overdue')
    fieldsets = (
        (None, {
            'fields': ('id', 'book', 'imprint', 'borrower')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )
    list_filter = ('status', 'due_back')
