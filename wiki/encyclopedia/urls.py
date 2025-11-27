from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("search", views.search, name="search"),
    path("new-entry", views.new, name="new-entry"),
    path("<str:title>", views.entry, name="entry"),
]