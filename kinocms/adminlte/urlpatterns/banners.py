from django.urls import path
from adminlte.views.banners import BannersView

app_name = "banners"

urlpatterns = [
    path("", BannersView.as_view(), name="index"),
]
