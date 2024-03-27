from django.urls import path

from adminlte.views.cinemas import CinemasView, CreateCinemaView, DeleteCinemaView

app_name = "cinemas"

urlpatterns = [
    path("", CinemasView.as_view(), name="index"),
    path("create/", CreateCinemaView.as_view(), name="create"),
    path("<int:cinema_id>/delete/", DeleteCinemaView.as_view(), name="delete"),
]
