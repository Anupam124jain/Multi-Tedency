from django.contrib import admin
from polls.models import Student,Books,Author
from tenants.utils import tenant_db_from_request


# Register your models here.
@admin.register(Student)
class PollAdmin(admin.ModelAdmin):
    fields = ["name", "age", "email", "password"]

    def get_queryset(self, request, *args, **kwargs):
        queryset = super().get_queryset(request, *args, **kwargs)
        tenant = tenant_db_from_request(request)
        queryset = queryset.filter(tenant=tenant)
        return queryset

    def save_model(self, request, obj, form, change):
        tenant = tenant_db_from_request(request)
        obj.tenant = tenant
        super().save_model(request, obj, form, change)


admin.site.register([Books,Author])