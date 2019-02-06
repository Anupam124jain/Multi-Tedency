from tenants.models import Tenant

def hostname_from_request(request):
    # split on `:` to remove port
    return request.get_host().split(":")[0].lower()

def tenant_db_from_request(request):
    hostname = hostname_from_request(request)
    tenants_map = get_tenants_map()
    return tenants_map.get(hostname)

def get_tenants_map():
    queryset = Tenant.objects.all()
    tanants_map = {}
    for i in range(len(queryset)):
        tanants_map.update({queryset[i].subdomain_prefix: queryset[i].db_name})
    return tanants_map
   