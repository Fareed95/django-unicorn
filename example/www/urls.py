from django.urls import path
from unicorn.components.direct_view import DirectViewView
from unicorn.components.redirects import RedirectsView
from www import views


app_name = "www"

urlpatterns = [
    path("", views.index, name="index"),
    path(
        "direct-view",
        DirectViewView.as_view(),
        name="direct-view",
    ),
    path(
        "redirects",
        RedirectsView.as_view(),
        name="redirects",
    ),
    path("<str:name>", views.template, name="template"),
]
