from .models import Postcard
from django.contrib.syndication.views import Feed
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import DetailView
from django.views.generic.list import ListView
from hitcount.views import HitCountDetailView
from copyrighter.models import Holder
from django.db.models import Q


class IndexView(ListView):
    model = Postcard
    paginate_by = 32

    def get_queryset(self):
        postcards = Postcard.objects.exclude(published="False")
        return postcards

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tags"] = Postcard.tags.tag_model.objects.weight()
        return context


class PostcardDetailView(HitCountDetailView):
    count_hit = True
    template_name = "detail.html"
    model = Postcard

    @property
    def originator(self):
        if self.kwargs.get("originator"):
            return Holder.objects.get(id=self.kwargs.get("originator"))
        else:
            return None

    @property
    def get_next_item_ID(self):
        p = Postcard.objects.filter(published=True).order_by("-id").all()
        if self.originator:
            p = p.filter(
                Q(photo_copyright__holder__id=self.originator.id)
                | Q(print_copyright__holder__id=self.originator.id)
            )
        next_id = p[0:1].get().id
        return next_id

    @property
    def get_previous_item_ID(self):
        p = Postcard.objects.filter(published=True).order_by("id").all()
        if self.originator:
            p = p.filter(
                Q(photo_copyright__holder__id=self.originator.id)
                | Q(print_copyright__holder__id=self.originator.id)
            )
        prev_id = p[0:1].get().id
        return prev_id

    def get_context_data(self, **kwargs):
        context = super(PostcardDetailView, self).get_context_data(**kwargs)
        context["originator"] = self.originator
        context["get_previous_item_ID"] = self.get_previous_item_ID
        context["get_next_item_ID"] = self.get_next_item_ID
        if self.object.postcarditem_set.all():
            context["postcards"] = self.object.postcarditem_set.all()
        return context

    def get_queryset(self):
        if self.originator:
            return Postcard.objects.filter(
                Q(photo_copyright__holder__id=self.originator.id)
                | Q(print_copyright__holder__id=self.originator.id)
            ).filter(published=True)
        else:
            return Postcard.objects.filter(published=True)


class OriginatorIndexView(ListView):
    model = Holder
    template_name = "originator_list.html"


class OriginatorDetailView(DetailView):
    model = Holder
    template_name = "originator_detail.html"

    def get_context_data(self, **kwargs):
        context = super(OriginatorDetailView, self).get_context_data(**kwargs)
        context["postcards"] = Postcard.objects.filter(published=True) & (
            Postcard.objects.filter(photo_copyright__holder__id=self.object.id)
            | Postcard.objects.filter(print_copyright__holder__id=self.object.id)
        )
        return context


class LatestPostcardsFeed(Feed):
    title = "Latest Cards"
    description = "Latest Items"
    link = "/"
    description_template = "feeds/postcards.html"

    def items(self):
        return Postcard.objects.exclude(published="False")

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description

    def item_link(self, item):
        return reverse("postcard_detail", args=[item.pk])

    def item_categories(self, item):
        return item.tags.tags

    def item_pubdate(self, item):
        if item.publishing_date:
            return item.publishing_date
        else:
            item.creation_timestamp
