from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect
from django.views.generic import TemplateView, CreateView, View

from adminlte.decorators import admin_only
from adminlte.forms.cinemas import CinemaForm, CinemaImageFormSet
from cinemas.models import Cinema


@admin_only
class CinemasView(TemplateView):
    template_name = "panel/cinemas/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cinemas'] = Cinema.objects.values('id', 'name_en', 'logo')
        return context


@admin_only
class CreateCinemaView(CreateView):
    template_name = "panel/cinemas/create.html"
    form_class = CinemaForm
    success_url = "cinemas:index"

    def get(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form()
        formset = CinemaImageFormSet()

        return self.render_to_response(
            self.get_context_data(form=form, formset=formset)
        )

    def post(self, request, *args, **kwargs):
        self.object = None
        form = CinemaForm(request.POST, request.FILES)
        formset = CinemaImageFormSet(request.POST, request.FILES)
        if form.is_valid() and formset.is_valid():
            cinema = form.save(commit=True)
            images = formset.save(commit=False)

            for image in images:
                image.cinema = cinema
                image.save()

            messages.success(request, "Cinema was created successfully")
            return redirect('cinemas:index')

        messages.error(request, "Some errors occurred while creating cinema")
        return redirect('cinemas:index')


@admin_only
class DeleteCinemaView(View):
    def post(self, request, cinema_id):
        try:
            Cinema.objects.filter(pk=cinema_id).delete()
            messages.success(request, "Cinema was successfully deleted")
        except ObjectDoesNotExist:
            messages.success(request, "Object does not exist")
        return redirect("cinemas:index")
