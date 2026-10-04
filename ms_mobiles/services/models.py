from django.db import models
import uuid


class ServiceRequest(models.Model):

    repair_id = models.CharField(
        max_length=20,
        unique=True,
        editable=False
    )

    # Customer Details
    customer_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)

    # Mobile Details
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=100)
    problem = models.TextField()

    # Repair Status
    status = models.CharField(
        max_length=30,
        default="Request Received"
    )

    # Delivery Agent / Mediator
    delivery_agent_name = models.CharField(
        max_length=100,
        default="Rahul Kumar"
    )

    delivery_agent_phone = models.CharField(
        max_length=15,
        default="9876501234"
    )

    pickup_status = models.CharField(
        max_length=30,
        default="Pickup Pending"
    )

    delivery_status = models.CharField(
        max_length=30,
        default="Not Delivered"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def save(self, *args, **kwargs):

        if not self.repair_id:
            self.repair_id = (
                "MSM-" +
                uuid.uuid4().hex[:8].upper()
            )

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.repair_id} - {self.customer_name}"