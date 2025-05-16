from django.contrib import admin
from resume.models import Resume
from markdownx.admin import MarkdownxModelAdmin

admin.site.register(Resume, MarkdownxModelAdmin)
