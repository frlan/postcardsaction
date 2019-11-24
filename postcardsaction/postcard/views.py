from django.shortcuts import render
from .models import Postcard
from django.views.generic.list import ListView
from django.views.generic import DetailView


class IndexView(ListView):
    model = Postcard
    paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tags"] = Postcard.tags.tag_model.objects.weight()
        return context


class PostcardDetailView(DetailView):
    template_name = "detail.html"
    model = Postcard
