from django.db import models


class Holder(models.Model):
    """
    A class to collect information about the holder
    (= who is having the copyright) of something
    """

    name = models.CharField(max_length=100)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Licence(models.Model):
    """
    A special typ of licence. This could be for example CC-BY-SA or GPLv3
    """

    slug = models.CharField(max_length=30)
    name = models.CharField(max_length=200)
    description = models.TextField(default="", blank=True)

    def __str__(self):
        return self.slug


class Copyright(models.Model):
    """
    A combination of a copyright holder is apply a special licence.

    This is what you actually want to connect to something that is listed
    under some copyright at all
    """

    holder = models.ForeignKey(Holder, on_delete=models.CASCADE)
    licence = models.ForeignKey(
        Licence, on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        if self.licence:
            return "{} ({})".format(self.holder, self.licence)
        else:
            return "{}".format(self.holder)

    class Meta:
        ordering = ["holder"]
