from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from upload.views import post_list, post_new, CreatePlayerSetView

urlpatterns = [
    path('', CreatePlayerSetView.as_view(template_name='post_list.html'), name='post_list'),
    path('post/new', post_new, name='post_new'),
    path("admin/", admin.site.urls),
]