from django.contrib import admin
from .models import *


# Register your models here.

class TagTublerInLine(admin.TabularInline):
    model = Tag

class PostAdmin(admin.ModelAdmin):
    inlines = [TagTublerInLine]
    list_display = ['tittle', 'author', 'date', 'status', 'section', 'Main_post']
    list_editable = ['status', 'section', 'Main_post']
    search_fields = ['tittle', 'author', 'section']

admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)