from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.urls import path, include, re_path
from django.views.generic.base import TemplateView
from postcard.views import IndexView
from postcard.views import PostcardDetailView
from postcard.views import LatestPostcardsFeed
from postcard.views import OriginatorDetailView
from postcard.views import OriginatorIndexView


urlpatterns = [
    re_path(r"^$", IndexView.as_view(template_name="index.html"), name="index"),
    re_path(r'^feed/$', LatestPostcardsFeed(), name='news_feed'),
    path("admin/", admin.site.urls),
    re_path(
        r"^(?P<pk>[\w]+)/$", PostcardDetailView.as_view(), name="postcard_detail",
    ),
    re_path(
        r"^o/(?P<pk>[\w]+)/$",
            OriginatorDetailView.as_view(),
            name="originator_detail"
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
