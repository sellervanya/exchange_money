from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


class CustomUserAdmin(UserAdmin):
    # add_form = CustomUserCreationForm
    # form = CustomUserChangeForm
    model = User
    list_display = ('id', 'username', 'email', 'document_id', 'is_active',)
    fieldsets = (
     (None, {'fields': ('username', 'password')}),
     ('Личные данные', {'fields': (
                                    'first_name', 'last_name', 'gender',
                                    'phone_number', 'document_id', 'email',
                                    )}),
     ('Службная информация', {'fields': (
                                'is_active', 'is_staff',
                                'is_superuser', 'groups',
                                'user_permissions')}),
     ('Важные даты', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
     (None, {
        'classes': ('wide',),
        'fields': (
                   'username', 'email', 'first_name',
                   'last_name', 'document_id', 'phone_number',
                   'gender', 'password1', 'password2')
                   }),
    )

    list_display_links = ('id', 'username', )
    search_fields = ('username', 'email', )
    ordering = ('id',)


admin.site.register(User, CustomUserAdmin)
