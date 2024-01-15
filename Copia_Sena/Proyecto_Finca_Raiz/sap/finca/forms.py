
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from .models import User
from django.utils.translation import gettext as _




class RoleOneCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ("username", "email", "password1", "password2")
        model = User

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Display name"
        self.fields["email"].label = "Email address"

    @transaction.atomic
    def save(self):
        user=super().save(commit=False)
        user.is_role1= True
        user.save()
        return user


class RoleTwoCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ("username", "email", "password1", "password2")
        model = User

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Display name"
        self.fields["email"].label = "Email address"

    @transaction.atomic
    def save(self):
        user=super().save(commit=False)
        user.is_role2= True
        user.save()
        return user

class RoleOneLogin(AuthenticationForm):
    def confirm_login_allowed(self,user):
        if not user.is_role1:
            raise forms.ValidationError(
                                        _("Username or password is incorrect!"),
                                        code="not_role1")

class RoleTwoLogin(AuthenticationForm):
    def confirm_login_allowed(self,user):
        if not user.is_role2:
            raise forms.ValidationError(
                                        _("Username or password is incorrect!"),
                                        code="not_role2")