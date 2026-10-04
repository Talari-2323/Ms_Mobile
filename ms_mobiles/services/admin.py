from django.contrib import admin
from .models import ServiceRequest


@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):

    list_display = (
        "repair_id",
        "customer_name",
        "phone",
        "brand",
        "model",
        "delivery_agent_name",
        "pickup_status",
        "status",
        "delivery_status",
        "created_at",
    )

    list_filter = (
        "status",
        "pickup_status",
        "delivery_status",
        "brand",
    )

    search_fields = (
        "repair_id",
        "customer_name",
        "phone",
        "delivery_agent_name",
    )

    readonly_fields = (
        "repair_id",
        "created_at",
    )

    fieldsets = (

        (
            "Repair Information",
            {
                "fields": (
                    "repair_id",
                    "status",
                    "created_at",
                )
            }
        ),

        (
            "Customer Details",
            {
                "fields": (
                    "customer_name",
                    "phone",
                )
            }
        ),

        (
            "Mobile Details",
            {
                "fields": (
                    "brand",
                    "model",
                    "problem",
                )
            }
        ),

        (
            "Delivery Agent / Mediator",
            {
                "fields": (
                    "delivery_agent_name",
                    "delivery_agent_phone",
                    "pickup_status",
                    "delivery_status",
                )
            }
        ),

    )