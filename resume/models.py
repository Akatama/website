from django.db import models
from django.core.exceptions import ValidationError
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify


class Resume(models.Model):
    body = MarkdownxField()

    class Meta:
        verbose_name_plural = "Resume"

    def save(self, *args, **kwargs):
        """
        Create only one Resume instance
        """
        if not self.pk and Resume.objects.exists():
            raise ValidationError(
                "There can only be one Resume, you cannot add another"
            )
            return None
        return super(Resume, self).save(*args, **kwargs)

    @property
    def formatted_markdown(self):
        return markdownify(self.body)
