from django.db import models


class Holder(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.name


class Licence(models.Model):
    slug = models.CharField(max_length=30)
    name = models.CharField(max_length=200)
    description = models.TextField(default="", blank=True)

    def __str__(self):
        return self.slug


class Copyright(models.Model):
    holder = models.ForeignKey(Holder, on_delete=models.CASCADE)
    licence = models.ForeignKey(
        Licence, on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        if self.licence:
            return "{} ({})".format(self.holder, self.licence)
        else:
            return "{}".format(self.holder)
