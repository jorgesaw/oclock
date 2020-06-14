"""User model admin."""

# Django
from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm

# Models
from apps.users.models import User, Profile



class CustomUserCreationForm(UserCreationForm):
    """Custom user creation form."""

    email = forms.EmailField(
        required=True, 
        help_text="Requerido, 254 caracteres como máximo y debe ser válido."
    )
    first_name = forms.CharField(
        label='Nombre', 
        max_length=255, 
        required=True, 
        help_text="Requerido, 255 caracteres como máximo y debe ser válido."
    )
    last_name = forms.CharField(
        label='Apellido', 
        max_length=255, 
        required=True, 
        help_text="Requerido, 255 caracteres como máximo y debe ser válido."
    )

    class Meta(UserCreationForm.Meta):
        fields = ('email', 'first_name', 'last_name')


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 
                'password2', 'first_name', 'last_name'),
        }),
    )
    list_display = ('email', 'username', 'first_name', 'last_name', 'is_staff', 'is_client')
    list_filter = ('is_client', 'is_staff', 'created', 'modified')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile model admin."""

    list_display = ('user', 'picture', 'biography')
    search_fields = ('user__username', 'user__email', 'user__first_name', 'user__last_name')
    list_filter = ()

