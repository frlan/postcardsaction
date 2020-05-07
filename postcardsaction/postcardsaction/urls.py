"""postcardsaction URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.urls import path, include
from django.views.generic.base import TemplateView
from postcard.views import IndexView
from postcard.views import PostcardDetailView
from postcard.views import LatestPostcardsFeed


urlpatterns = [
    url(r"^$", IndexView.as_view(template_name="index.html"), name="index"),
    url(r'^feed/$', LatestPostcardsFeed(), name='news_feed'),
    path("admin/", admin.site.urls),
    path("markdown/", include("django_markdown.urls")),
    url(
        r"^(?P<pk>[\w]+)/$",
        PostcardDetailView.as_view(),
        name="postcard_detail",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
