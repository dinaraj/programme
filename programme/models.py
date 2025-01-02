from django.db import models
from ckeditor.fields import RichTextField


"""class Lieu(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='/lieux')
"""


class Programme(models.Model):

    FONT_CHOICES = [
        ('Times New Roman', 'Times New Roman'),
        ('Arial', 'Arial'),
    ]
    date = models.DateField()
    content = RichTextField()
    nb_views = models.PositiveIntegerField(default=0)
    # lieu = models.ForeignKey(Lieu, on_delete=models.SET_NULL, null=True)
    font_family = models.CharField(max_length=50, choices=FONT_CHOICES, default='Arial')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.date)

    class Meta:
        ordering = ['-created_at']
