from datetime import date, timedelta

from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, Expression, F, Sum
from django.shortcuts import redirect, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, CreateView

from adminlte.decorators import admin_only
from adminlte.forms.films import FilmForm, FilmImageFormSet
from films.models import Film


@admin_only
class EditFilmView(TemplateView):
    template_name = "panel/films/edit.html"

    def get(self, request, film_id):
        film = get_object_or_404(Film, pk=film_id)
        form = FilmForm(instance=film)
        formset = FilmImageFormSet(instance=film)
        return self.render_to_response(self.get_context_data(form=form, formset=formset, film=film))

    def post(self, request, film_id):
        film = get_object_or_404(Film, pk=film_id)
        form = FilmForm(request.POST, request.FILES, instance=film)
        formset = FilmImageFormSet(request.POST, request.FILES, instance=film)

        if form.is_valid() and formset.is_valid():
            form.save(commit=True)
            formset.save(commit=True)

            messages.success(request, "Film was edited successfully")
            return redirect('films:index')

        messages.error(request, "Some errors occurred while editing film")
        return self.render_to_response(self.get_context_data(form=form, formset=formset, film=film))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(kwargs)
        return context


@admin_only
class DeleteFilmView(View):
    def post(self, request, film_id):
        try:
            Film.objects.filter(pk=film_id).delete()
            messages.success(request, "Film was successfully deleted")
        except ObjectDoesNotExist:
            messages.success(request, "Object does not exist")
        return redirect("films:index")


@admin_only
class FilmsView(TemplateView):
    template_name = "panel/films/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        today = date.today()

        current_films = Film.objects.annotate(
            release_date=F('created_at') + timedelta(days=7),
            end_date=F('created_at') + timedelta(days=30),
        ).filter(
            Q(release_date__lte=today) & Q(end_date__gte=today),
        ).values('id', 'name_en', 'image')
        context['current_films'] = current_films

        upcoming_films = Film.objects.annotate(
            release_date=F('created_at') + timedelta(days=7),
        ).filter(release_date__gt=today).values('id', 'name_en', 'image')
        context['upcoming_films'] = upcoming_films

        return context


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

    def post(self, request, *args, **kwargs):
        self.object = None
        form = FilmForm(request.POST, request.FILES)
        formset = FilmImageFormSet(request.POST, request.FILES)

        if form.is_valid() and formset.is_valid():
            film = form.save(commit=True)
            images = formset.save(commit=False)

            for image in images:
                image.film = film
                image.save()

            messages.success(request, "Film was created successfully")
            return redirect('films:index')

        messages.error(request, "Some errors occurred while creating film")
        return redirect('films:index')
