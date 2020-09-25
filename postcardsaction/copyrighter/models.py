from django.db import models


class Holder(models.Model):
    """
    A class to collect information about the holder
    (= who is having the copyright) of something
    """

    name = models.CharField(
        max_length=100, help_text="Ust it for (transcripted) writing of name.")
    org_name = models.CharField(
        max_length=100,
        help_text="Use for native writing of the name e.g. in Cyrillic.",
        blank=True,
        null=True)
    url = models.URLField(blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=50, blank=True)
    address = models.TextField(
        blank=True,
        help_text="May contain free-text address data for the copyright holder"
    )

    def __str__(self):
        if self.org_name:
            return "{}({})".format(self.org_name, self.name)
        else:
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
    licence = models.ForeignKey(Licence,
                                on_delete=models.CASCADE,
                                null=True,
                                blank=True)
    year = models.IntegerField(blank=True, null=True)

    def __str__(self):
        _tmp = [self.holder.__str__()]
        if self.licence:
            _tmp.append(self.licence.__str__())
        if self.year:
            _tmp.append("({})".format(self.year))
        return ' '.join(_tmp)

    class Meta:
        ordering = ["holder"]
