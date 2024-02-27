from django.urls import path
from adminlte.views.banners import BannersView, BackgroundSettingsView

app_name = "banners"

urlpatterns = [
    path("", BannersView.as_view(), name="index"),
    path("background-settings/", BackgroundSettingsView.as_view(), name="background-settings")
]
