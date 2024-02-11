from django.urls import path, include

urlpatterns = [
    path("authentication/", include("adminlte.urlpatterns.authentication", namespace="authentication")),
    path("dashboard/", include("adminlte.urlpatterns.dashboard", namespace="dashboard")),
    path("banners/", include("adminlte.urlpatterns.banners", namespace="banners"))
]
