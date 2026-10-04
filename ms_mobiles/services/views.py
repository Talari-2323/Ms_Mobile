from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.core.mail import send_mail

from .models import ServiceRequest


def home(request):
    return render(request, "home.html")


def service_request(request):

    if request.method == "POST":

        service = ServiceRequest.objects.create(
            customer_name=request.POST.get("customer_name"),
            phone=request.POST.get("phone"),
            brand=request.POST.get("brand"),
            model=request.POST.get("model"),
            problem=request.POST.get("problem"),
        )

        return render(
            request,
            "home.html",
            {
                "success": True,
                "service": service,
            }
        )

    return render(request, "home.html")


def track_repair(request):

    service = None
    error = None

    if request.method == "POST":

        repair_id = request.POST.get(
            "repair_id", ""
        ).strip().upper()

        try:
            service = ServiceRequest.objects.get(
                repair_id=repair_id
            )

        except ServiceRequest.DoesNotExist:

            error = "Repair ID not found. Please check your ID."

    return render(
        request,
        "home.html",
        {
            "tracked_service": service,
            "track_error": error,
        }
    )


# LOGIN VIEW
def user_login(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            # Send login notification email
            send_mail(
                "MS Mobiles - Login Notification",
                f"""
Hello {user.username},

You have successfully logged in to MS Mobiles.

Username: {user.username}

Thank you for using MS Mobiles.
""",
                "thalariaparna.2323@gmail.com",
                [user.email],
                fail_silently=False,
            )

            messages.success(
                request,
                "Login successful! A login notification has been sent to your email."
            )

            return redirect("home")

        else:

            messages.error(
                request,
                "Invalid username or password."
            )

    return render(request, "login.html")