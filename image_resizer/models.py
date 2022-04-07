from django.db import models
from stdimage import StdImageField, JPEGField

# Create your models here.


class ImageResizer(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    species = models.CharField(max_length=100, blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    length = models.FloatField(blank=True, null=True)
    latitude = models.CharField(max_length=100, blank=True, null=True)
    longitude = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateField(auto_now_add=True, auto_now=False)
    image = StdImageField(upload_to='images/', blank=True, null=True, variations={
        'large': (1200, 1200),
        'thumbnail': (150, 150, True),
        'small': (300, 300),
        'medium': (600, 600),
    }, delete_orphans=True)

    class Meta:
        db_table = 'image_resizer'

    def __str__(self):
        return str(self.name)
