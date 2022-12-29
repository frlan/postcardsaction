from django.db import models


class POI(models.Model):

    name = models.CharField(max_length=50, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    urls = models.ManyToManyField("postcard.URL", related_name="poi", blank=True)

    def __str__(self):
        return self.name
