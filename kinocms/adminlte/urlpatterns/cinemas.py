from django.urls import path

from adminlte.views.cinemas import CinemasView, CreateCinemaView

app_name = "cinemas"

urlpatterns = [
    path("", CinemasView.as_view(), name="index"),
    path("create/", CreateCinemaView.as_view(), name="create"),
]
