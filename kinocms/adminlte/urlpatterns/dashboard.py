from django.urls import path
from adminlte.views.dashboard import DashboardView

app_name = "dashboard"

urlpatterns = [
    path("", DashboardView.as_view(), name="index"),
]
