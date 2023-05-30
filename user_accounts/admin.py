'''
Accounts Administrator Panel
'''

# Import all requirements
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import user_accounts


# Custom user administrator class
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = user_accounts
    list_display = ['id', 'email', 'username','is_staff']
    search_fields = ['id', 'email', 'username', 'full_name']
    list_filter = ('is_staff', 'is_superuser', 'groups')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),

    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'full_name', 'password1', 'password2', 'is_staff', 'is_superuser', 'is_active', 'groups', 'user_permissions')}
         ),
    )
    ordering = ('id','is_staff')


# Register custom User administrator Class
admin.site.register(user_accounts, CustomUserAdmin)
