from django.urls import path, include

urlpatterns = [
    path("authentication/", include("adminlte.urlpatterns.authentication", namespace="authentication")),
    path("dashboard/", include("adminlte.urlpatterns.dashboard", namespace="dashboard")),
    path("banners/", include("adminlte.urlpatterns.banners", namespace="banners")),
    path("films/", include("adminlte.urlpatterns.films", namespace="films")),
    path("cinemas/", include("adminlte.urlpatterns.cinemas", namespace="cinemas"))
]
