from django.urls import path
from adminlte.views.films import FilmsView, CreateFilmView, DeleteFilmView

app_name = "films"

urlpatterns = [
    path("", FilmsView.as_view(), name="index"),
    path("create/", CreateFilmView.as_view(), name="create"),
    path("<int:film_id>/delete/", DeleteFilmView.as_view(), name="delete"),
]
