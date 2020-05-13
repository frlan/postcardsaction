# class Tag:
#   - extern
#
# class Images/Gallery
#   - extern
#
# class URLs
#   - extern
#       - django-linkcheck
#
# class Copyright
#   -> publisher
#   -> fotographer
#
# class Postcard
#   -> Tag
#   -> Images
#   -> URLs
#
#   -> year received
#   -> status (new, sent, …)
#   -> description
#   -> description_short
#   -> copyright information
#   -> swapping
#   -> owner
#   -> comment
#
# class Owner
#   -> nick
#
# class Collection
#   -> Postcard
#
from django.db import models
from django_markdown.models import MarkdownField
from stdimage import StdImageField, JPEGField
import datetime
import tagulous.models
from copyrighter.models import Copyright
from postcrossing.models import PCPostCard
from django.urls import reverse


class Tag(tagulous.models.TagTreeModel):
    class TagMeta:
        force_lowercase = False


class URLTag(tagulous.models.TagTreeModel):
    class TagMeta:
        force_lowercase = False


class URL(models.Model):

    title = models.CharField(
        max_length=100, help_text="A short description/title of the URL",
    )
    url = models.URLField(max_length=250)
    tags = tagulous.models.TagField(to=URLTag)

    def __str__(self):
        return self.title


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
    last_udpated = models.DateTimeField(auto_now=True)

    tags = tagulous.models.TagField(to=Tag)
    photo_copyright = models.ManyToManyField(Copyright, related_name="photo")
    print_copyright = models.ManyToManyField(Copyright, related_name="print")

    urls = models.ManyToManyField(
        URL, related_name="further_information", blank=True)

    published = models.BooleanField(
        default=False,
        help_text="Whether this postcard is visible."
    )

    def __str__(self):
        return self.description_short

    def get_absolute_url(self):
        return reverse("postcard_detail", kwargs={"slug": str(self.slug)})

    class Meta:
        ordering = ["-id"]


class PostcardItem(models.Model):

    postcard = models.ForeignKey(
        Postcard, on_delete=models.CASCADE)
    postcrossing = models.ForeignKey(
        PCPostCard, on_delete=models.CASCADE, null=True, blank=True)
    swapping = models.BooleanField(
        default=False,
        help_text="Whether this postcard is free for private swapping",
    )
    year_recieved = models.DateField("Date", default=datetime.date.today)
    year_verified = models.BooleanField(
        default=True, help_text="Whether the year of recieving is verified"
    )

    creation_timestamp = models.DateTimeField(auto_now_add=True)
    last_udpated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["id"]
