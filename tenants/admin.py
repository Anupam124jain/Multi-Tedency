""" Admin Registration page """
import os
from django.contrib import admin
from multi_tedency.settings import BASE_DIR
from .models import Tenant
from multi_tedency import settings
from multi_tedency.db_create import db_create

script_path = os.path.join(BASE_DIR, 'manage_host.sh')
create_database_path = os.path.join(BASE_DIR, 'create_database.sh')

# Actions of Admin
def activate_selected(modeladmin, request, queryset):
    client_domain = queryset[0].subdomain_prefix
    if not queryset[0].is_active:
            os.system(
            'echo ranosys|sudo -S bash {0} activate {1}'.format(script_path,
                client_domain))
    queryset.update(is_active=True)

activate_selected.short_description = "Activate client"



def deactivate_selected(modeladmin, request, queryset):
    client_domain = queryset[0].subdomain_prefix
    if queryset[0].is_active:
        os.system(
            'echo ranosys|sudo -S bash {0} deactivate {1}'.format(script_path,
                client_domain))
    queryset.update(is_active=False)

deactivate_selected.short_description = "Deactivate client"

def createdatabase_selected(modeladmin, request, queryset):
    db_name = queryset[0].db_name
    db_create(db_name)
    os.system('echo ranosys|sudo -S bash {0} {1} {2} {3}'.format(create_database_path, db_name, 'root', 'ranosys'))

createdatabase_selected.short_description = "Create Database"


class tenentAdmin(admin.ModelAdmin):
    list_display = ['db_name', 'is_active']
    actions = [activate_selected, deactivate_selected, createdatabase_selected]


# Register your models here.
admin.site.register(Tenant,tenentAdmin)
