from django.views.generic import TemplateView

from adminlte.decorators import admin_only


@admin_only
class FilmsView(TemplateView):
    template_name = "panel/films/index.html"


@admin_only
class CreateFilmView(TemplateView):
    template_name = "panel/films/create.html"
