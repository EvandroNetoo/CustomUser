from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User


class CustomUserAdmin(UserAdmin):
    add_form_template = None
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': (
                    'username',
                    'cpf',
                    'endereco',
                    'telefone',
                    'password1',
                    'password2',
                ),
            },
        ),
    )
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Complemento do Usuário',
            {
                'fields': (
                    'cpf',
                    'telefone',
                    'endereco',
                )
            },
        ),
    )


admin.site.register(User, CustomUserAdmin)
