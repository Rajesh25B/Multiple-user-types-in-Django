from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    class Types(models.TextChoices):
        CUSTOMER = "CUSTOMER", "Customer"
        DRIVER = "DRIVER", "Driver"
        STAFF = "STAFF", "Staff"

    base_type = Types.CUSTOMER

    # What type of user are we?
    type = models.CharField(
        _("Type"), max_length=50, choices=Types.choices, default=base_type
    )

    # First Name and Last Name Do Not Cover Name Patterns
    # Around the Globe.
    name = models.CharField(_("Name of User"), blank=True, max_length=255)

    def get_absolute_url(self):
        return reverse("accounts:detail", kwargs={"username": self.username})


class Customer(User):
    class Meta:
        proxy = True


class Driver(User):
    class Meta:
        proxy = True


class Staff(User):
    class Meta:
        proxy = True
