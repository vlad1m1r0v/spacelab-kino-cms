from django.views.generic import TemplateView

from adminlte.decorators import admin_only


@admin_only
class BannersView(TemplateView):
    template_name = "panel/banners.html"
