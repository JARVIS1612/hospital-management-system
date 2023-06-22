from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm
from .models import Users, Doctors, Pharma


# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    model = Users
    list_display = ['username',
                    'first_name',
                    'last_name',
                    'number',
                    'blood_group',
                    'date_time',
                    'is_patient',
                    'is_doctor',
                    'is_pharma']
    fieldsets = (
        (None, {
            'fields': (
                'email', 'first_name', 'last_name', 'username', 'number', 'gender', 'age', 'blood_group', 'date_time', 'is_patient',
                'is_doctor', 'is_pharma')
        }),)


admin.site.register(Users, CustomUserAdmin)
admin.site.register(Doctors)
admin.site.register(Pharma)