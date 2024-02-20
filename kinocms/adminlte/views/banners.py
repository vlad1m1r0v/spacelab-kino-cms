from django.views.generic import TemplateView
from django.forms import modelformset_factory
from adminlte.decorators import admin_only
from adminlte.forms.banners import TopBannerForm, TopBannerSettingsForm
from banners.models import TopBanner, BannerSettings


@admin_only
class BannersView(TemplateView):
    template_name = "panel/banners.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        initial_settings = BannerSettings.objects.all().first()
        context["top_banner_settings_form"] = TopBannerSettingsForm(
            initial={'banner_rotation': initial_settings.banner_rotation,
                     'are_banners_active': initial_settings.are_banners_active})

        top_banner_formset = modelformset_factory(TopBanner, form=TopBannerForm, extra=1)
        context["top_banner_formset"] = top_banner_formset(queryset=TopBanner.objects.all(), prefix="top_banner")

        return context
