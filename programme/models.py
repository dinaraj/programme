from django.db import models
from ckeditor.fields import RichTextField


class Programme(models.Model):
    date = models.DateField()
    content = RichTextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.date)

    class Meta:
        ordering = ['-created_at']
