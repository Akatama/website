from django.contrib import admin
from about_me.models import AboutMe
from markdownx.admin import MarkdownxModelAdmin

admin.site.register(AboutMe, MarkdownxModelAdmin)
