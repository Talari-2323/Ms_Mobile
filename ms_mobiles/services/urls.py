from django.urls import path
from . import views


urlpatterns = [
    path(
        "service-request/",
        views.service_request,
        name="service_request"
    ),

   

    path(
        "login/",
        views.user_login,
        name="login"
    ),
]
