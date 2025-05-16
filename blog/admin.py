from django.contrib import admin
from blog.models import Category, Post
from markdownx.admin import MarkdownxModelAdmin


class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Category, CategoryAdmin)

admin.site.register(Post, MarkdownxModelAdmin)
