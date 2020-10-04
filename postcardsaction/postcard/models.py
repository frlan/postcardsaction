from copyrighter.models import Copyright
from django.db import models
from django_markdown.models import MarkdownField
from django.urls import reverse
from postcrossing.models import PCPostCard
from stdimage import StdImageField, JPEGField
import datetime
import django.utils.timezone
import tagulous.models


class Tag(tagulous.models.TagTreeModel):
    class TagMeta:
        force_lowercase = False


class URLTag(tagulous.models.TagTreeModel):
    class TagMeta:
        force_lowercase = False


class URL(models.Model):

    title = models.CharField(
        max_length=100,
        help_text="A short description/title of the URL",
    )
    url = models.URLField(max_length=250)
    tags = tagulous.models.TagField(to=URLTag)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["title"]


class Series(models.Model):
    title = models.CharField(max_length=100)
    description = MarkdownField(default="", blank=True)

    urls = models.ManyToManyField(URL,
                                  related_name="series_links",
                                  blank=True)
    def __str__(self):
        return self.title

    class Meta:
        ordering = ["title"]
        verbose_name_plural = "Series"


class Postcard(models.Model):

    description_short = models.CharField(
        max_length=100,
        help_text="Short description of the card may be used as a teaser",
        default="",
    )
    description = MarkdownField(
        default="",
        help_text="""Actual description for a postcard:
            * some story behind
            * where came it from
            * what to see""",
    )
    image = StdImageField(
        upload_to="img/postcardimages",
        blank=True,
        variations={
            "large": (1024, 1024),
            "thumbnail": (150, 150, False),
            "medium": (600, 600),
        },
        delete_orphans=True,
    )

    creation_timestamp = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    tags = tagulous.models.TagField(to=Tag)
    photo_copyright = models.ManyToManyField(Copyright, related_name="photo")
    print_copyright = models.ManyToManyField(Copyright, related_name="print")

    urls = models.ManyToManyField(URL,
                                  related_name="further_information",
                                  blank=True)

    published = models.BooleanField(
        default=False, help_text="Whether this postcard is visible.")
    publishing_date = models.DateTimeField(default=django.utils.timezone.now,
                                           null=True,
                                           blank=True)
    series = models.ManyToManyField(Series,
                                    related_name="series_member",
                                    blank=True)

    def __str__(self):
        return self.description_short

    def get_absolute_url(self):
        return reverse("postcard_detail", kwargs={"slug": str(self.slug)})

    class Meta:
        ordering = ["-id"]


class PostcardItem(models.Model):

    postcard = models.ForeignKey(Postcard, on_delete=models.CASCADE)
    postcrossing = models.ForeignKey(PCPostCard,
                                     on_delete=models.CASCADE,
                                     null=True,
                                     blank=True)
    swapping = models.BooleanField(
        default=False,
        help_text="Whether this postcard is free for private swapping",
    )
    year_received = models.DateField("Date", default=datetime.date.today)
    year_verified = models.BooleanField(
        default=True, help_text="Whether the year of receiving is verified")

    creation_timestamp = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.postcrossing:
            return "{} ({})".format(self.postcard.description_short,
                                    self.postcrossing.pc_id)
        else:
            return self.postcard.description_short

    class Meta:
        ordering = ["id"]
