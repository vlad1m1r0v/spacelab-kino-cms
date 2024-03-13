from django.views.generic import TemplateView, CreateView

from adminlte.decorators import admin_only
from adminlte.forms.films import FilmForm, FilmImageFormSet


@admin_only
class FilmsView(TemplateView):
    template_name = "panel/films/index.html"


@admin_only
class CreateFilmView(CreateView):
    template_name = "panel/films/create.html"
    form_class = FilmForm
    success_url = "films:index"

    def get(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        formset = FilmImageFormSet()

        return self.render_to_response(
            self.get_context_data(form=form, formset=formset)
        )
