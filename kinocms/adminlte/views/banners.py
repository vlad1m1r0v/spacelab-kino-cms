from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import TemplateView, View
from adminlte.decorators import admin_only
from adminlte.forms.banners import (TopBannerSettingsForm, AdvertisementBannerSettingsForm,
                                    BannerSettingsForm, TopBannerFormSet, AdvertisementBannerFormset)
from banners.models import TopBanner, BannerSettings, AdvertisementBanner


@admin_only
class BannersView(TemplateView):
    template_name = "panel/banners.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        initial_settings = BannerSettings.objects.all().first()
        # top banner settings
        context["top_banner_settings_form"] = TopBannerSettingsForm(
            initial={'banner_rotation': initial_settings.banner_rotation,
                     'are_banners_active': initial_settings.are_banners_active},
            prefix="top_banner_settings")

        context["top_banner_formset"] = TopBannerFormSet(queryset=TopBanner.objects.all(),
                                                         prefix="top_banners")
        # background settings
        context["banner_settings_form"] = BannerSettingsForm(
            initial={
                "is_background_image": initial_settings.is_background_image,
                "background_image": initial_settings.background_image
            }
        )
        # advertisement banner settings
        context["advertisement_banner_settings_form"] = AdvertisementBannerSettingsForm(
            initial={'advertisement_rotation': initial_settings.advertisement_rotation,
                     'are_advertisements_active': initial_settings.are_advertisements_active},
            prefix="advertisement_banner_settings")

        context["advertisement_banner_formset"] = AdvertisementBannerFormset(
            queryset=AdvertisementBanner.objects.all(),
            prefix="advertisement_banners")

        return context


@admin_only
class BackgroundSettingsView(View):
    def post(self, request, *args, **kwargs):
        form = BannerSettingsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Background settings changed successfully")
        else:
            messages.error(request, form.non_field_errors().as_text()[2:])
        return redirect("banners:index")


@admin_only
class TopBannersView(View):
    def post(self, request, *args, **kwargs):
        top_banner_settings_form = TopBannerSettingsForm(request.POST, prefix="top_banner_settings")

        if top_banner_settings_form.is_valid():
            top_banner_settings_form.save()

        top_banner_formset = TopBannerFormSet(request.POST, request.FILES, prefix="top_banners")

        if top_banner_formset.is_valid():
            top_banner_formset.save()
            messages.success(request, "Top banners updated successfully")
        else:
            messages.error(request, "some fields are missing")

        return redirect("banners:index")
