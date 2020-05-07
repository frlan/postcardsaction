from django.contrib.syndication.views import Feed
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import DetailView
from django.views.generic.list import ListView
from hitcount.views import HitCountDetailView
from .models import Postcard


class IndexView(ListView):
    model = Postcard
    paginate_by = 100

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
    queryset = Postcard.objects.filter(published=True)


class LatestPostcardsFeed(Feed):
    title = "Latest Cards"
    description = "Latest Items"
    link = "/"
    description_template = "feeds/postcards.html"

    def items(self):
        return Postcard.objects.all()

    def item_title(self, item):
        return item.description_short

    def item_description(self, item):
        return item.description

    def item_link(self, item):
        return reverse('postcard_detail', args=[item.pk])

