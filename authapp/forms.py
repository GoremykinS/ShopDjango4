from django.contrib.auth.forms import (
    AuthenticationForm,
    UserChangeForm,
    UserCreationForm,
)
from django import forms
from .models import ShopUser


class ShopUserLoginForm(AuthenticationForm):
    class Meta:
        model = ShopUser
        fields = ("username", "password")

    error_css_class = "has-error"

    def __init__(self, *args, **kwargs):
        super(ShopUserLoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"


class ShopUserEditForm(UserChangeForm):
    class Meta:
        model = ShopUser
        fields = (
            "username",
            "first_name",
            "email",
            "city",
            "phone_number",
            "avatar",
            "password",
        )

    error_css_class = "haserror"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"
            field.help_text = ""
            if field_name == "password":
                field.widget = forms.HiddenInput()

    def clean_city(self):
        data = self.cleaned_data["city"]
        if data != "Казань":
            raise forms.ValidationError("Только для жителей Казани")
        return data


class ShopUserRegisterForm(UserCreationForm):
    class Meta:
        model = ShopUser
        fields = (
            "username",
            "first_name",
            "password1",
            "password2",
            "phone_number",
            "email",
            "city",
        )


def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    for field_name, field in self.fields.items():
        field.widget.attrs["class"] = "form-control"
        field.help_text = ""


def clean_city(self):
    data = self.cleaned_data["city"]
    if data != "Казань":
        raise forms.ValidationError("Только для жителей Казани")
    return data
