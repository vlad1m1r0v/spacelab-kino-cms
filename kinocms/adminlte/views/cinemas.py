from django.views.generic import TemplateView, CreateView

from adminlte.decorators import admin_only


@admin_only
class CinemasView(TemplateView):
    template_name = "panel/cinemas/index.html"


@admin_only
class CreateCinemaView(TemplateView):
    template_name = "panel/cinemas/create.html"
