from django.urls import path
from . import views


urlpatterns = [
    path(
        "service-request/",
        views.service_request,
        name="service_request"
    ),

    path(
        "track-repair/",
        views.track_repair,
        name="track_repair"
    ),

    path(
        "login/",
        views.user_login,
        name="login"
    ),
]