from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Client


class CustomUserCreation(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Client
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'picture')


class CustomUSerChange(UserChangeForm):
    class Meta:
        fields = UserChangeForm.Meta.fields