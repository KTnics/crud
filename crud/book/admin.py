from django.contrib import admin
from .models import Books


class BooksAdmin(admin.ModelAdmin):
    list_display = ['id','author','name','description','price',]

admin.site.register(Books,BooksAdmin)
