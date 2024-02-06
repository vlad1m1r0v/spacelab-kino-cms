from django.views.generic import TemplateView

from adminlte.decorators import admin_only


@admin_only
class DashboardView(TemplateView):
    template_name = "panel/dashboard.html"
