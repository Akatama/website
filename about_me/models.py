from django.db import models
from django.core.exceptions import ValidationError
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify


class AboutMe(models.Model):
    title = models.CharField(max_length=255)
    body = MarkdownxField()

    def save(self, *args, **kwargs):
        """
        Create only one About Me instance
        """
        if not self.pk and AboutMe.objects.exists():
            raise ValidationError(
                "There can only be one About Me, you cannot add another"
            )
            return None
        return super(AboutMe, self).save(*args, **kwargs)

    @property
    def formatted_markdown(self):
        return markdownify(self.body)
