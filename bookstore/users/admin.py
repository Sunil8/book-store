from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from users.forms import UserChangeForm, UserCreationForm
from users.models import User

class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'username', 'is_active', 'is_superuser')
    list_filter = ('is_superuser',)

    fieldsets = (
        (None, {'fields':('password',)}),
        ('Personal Info', {'fields':('email','username',)}),
        ('Permissions',{'fields':('is_superuser', 'is_active')}),
    )
    
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(User, UserAdmin)

