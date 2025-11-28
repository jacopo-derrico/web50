from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("404", views.error, name="error"),
    path("search", views.search, name="search"),
    path("new-entry", views.new, name="new-entry"),
    path("random_page", views.random_page, name="random_page"),
    path("edit/<str:title>", views.edit, name="edit"),
    path("<str:title>", views.entry, name="entry"),
]