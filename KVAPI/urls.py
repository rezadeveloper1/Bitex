from django.urls import path
from . import views

urlpatterns = [
    path("key/", views.KeyValueApi.as_view(), name="key"),
    path("key/<int:pk>", views.KeyValueDetailID.as_view(), name="Update-or-Read"),
    path("key/<slug:slug>", views.KeyValueDetailSlug.as_view(), name="key-value-slug"),
    path("history/<slug:slug>", views.KeyValueHistory.as_view(), name="history-key"),

    path("", views.HomeView.as_view(), name="home"),
    path("view/key", views.KeyView.as_view(), name="key-view"),
    path("view/key/<slug:slug>", views.KeyValueDetail.as_view(), name="key-with-slug"),
    path("view/history", views.KeyValueHistoryEn.as_view(), name="hostory-key-enter"),
    path("view/history/<slug:slug>", views.KeyValueHistory.as_view(), name="hostory-key"),
    path("view/set", views.KeyValueSet.as_view(), name="set-key-value"),
]
