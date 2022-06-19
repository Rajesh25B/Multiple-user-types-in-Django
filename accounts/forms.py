from django.contrib.auth import get_user_model, forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from django import forms as d_forms
from allauth.account.forms import SignupForm

User = get_user_model()

# AccountSignupForm inherits from django-allauth's SignupForm
class AccountSignupForm(SignupForm):

    # Specify a choice field that matches the choice field on our user model
    type = d_forms.ChoiceField(
        choices=[
            ("CUSTOMER", "Customer"),
            ("DRIVER", "Driver"),
            ("STAFF", "Staff"),
        ]
    )

    # Override the init method
    def __init__(self, *args, **kwargs):
        # Call the init of the parent class
        super().__init__(*args, **kwargs)

    # Put in custom signup logic
    def custom_signup(self, request, user):
        # Set the user's type from the form reponse
        user.type = self.cleaned_data["type"]
        # Save the user's type to their database record
        user.save()
