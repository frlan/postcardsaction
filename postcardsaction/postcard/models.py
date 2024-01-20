from copyrighter.models import Copyright
from django.db import models

# from django_markdown.models import MarkdownField
from django.urls import reverse
from postcrossing.models import PCPostCard
from stdimage import StdImageField, JPEGField
import datetime
import django.utils.timezone
import tagulous.models
from django.db.models import Q
from poi.models import POI


class Tag(tagulous.models.TagTreeModel):
    class TagMeta:
        force_lowercase = False


class URL(models.Model):
    title = models.CharField(
        max_length=100,
        help_text="A short description/title of the URL",
    )
    url = models.URLField(
        max_length=250,
        verbose_name="URL",
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["title"]
        unique_together = [["title", "url"]]
        verbose_name = "URL"
        verbose_name_plural = "URLs"


class Series(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(default="", blank=True)

    urls = models.ManyToManyField(URL, related_name="series_links", blank=True)
    publisher = models.ManyToManyField(Copyright, related_name="publisher", blank=True)
    logo = StdImageField(
        upload_to="img/series",
        blank=True,
        variations={
            "large": (1024, 1024),
            "medium": (600, 600),
            "small": (300, 300),
            "thumbnail": (150, 150, False),
        },
        delete_orphans=True,
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["title"]
        verbose_name_plural = "Series"


class Country(models.Model):
    iso_code = models.CharField(max_length=10, help_text="ISO of country", default="")

    def __str__(self):
        return self.iso_code

    class Meta:
        verbose_name_plural = "Countries"
        ordering = ["iso_code"]


class Postcard(models.Model):
    title = models.CharField(
        max_length=100,
        help_text="Title of the postcard",
        default="",
    )

    subtitle = models.CharField(
        max_length=100, help_text="A subtitle for the postcard", null=True, blank=True
    )

    description = models.TextField(
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
            "medium": (600, 600),
            "small": (300, 300),
            "thumbnail": (150, 150, False),
        },
        delete_orphans=True,
    )

    poi = models.ManyToManyField(
        POI,
        blank=True,
        verbose_name="POI",
    )

    image_description = models.TextField(
        blank=True,
        null=True,
        help_text="""
            A more formal description of the image for visual
            handicapped people -- a description that might not fit to
            the main text
        """,
    )

    backside_description_text = models.TextField(
        default="",
        blank=True,
        null=True,
        help_text=(
            "The text on the back of a postcard explaining " "what's printed there."
        ),
    )

    country_of_origin = models.ForeignKey(
        Country,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text="Country of origin if known.",
    )

    creation_timestamp = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    tags = tagulous.models.TagField(to=Tag)

    photo_copyright = models.ManyToManyField(Copyright, related_name="photo")
    print_copyright = models.ManyToManyField(Copyright, related_name="print")

    urls = models.ManyToManyField(
        URL,
        related_name="further_information",
        blank=True,
        verbose_name="URLs",
    )

    published = models.BooleanField(
        default=False, help_text="Whether this postcard is visible."
    )
    publishing_date = models.DateTimeField(
        default=django.utils.timezone.now, null=True, blank=True
    )
    series = models.ManyToManyField(Series, related_name="series_member", blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("postcard_detail", kwargs={"slug": str(self.slug)})

    class Meta:
        ordering = ["-id"]


class PostcardItem(models.Model):
    postcard = models.ForeignKey(Postcard, on_delete=models.CASCADE)
    postcrossing = models.ForeignKey(
        PCPostCard, on_delete=models.CASCADE, null=True, blank=True
    )
    swapping = models.BooleanField(
        default=False,
        help_text="Whether this postcard is free for private swapping",
    )
    year_received = models.DateField("Date", default=datetime.date.today)
    year_verified = models.BooleanField(
        default=True, help_text="Whether the year of receiving is verified"
    )

    creation_timestamp = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.postcrossing:
            return "{} ({})".format(self.postcard.title, self.postcrossing.pc_id)
        else:
            return self.postcard.title

    class Meta:
        ordering = ["id"]
