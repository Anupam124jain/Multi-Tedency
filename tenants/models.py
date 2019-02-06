from django.db import models

ROLES = {
    (1," "),
    ("Product", "Product"),
    ("Risk", "Risk"),
    ("Marketing", "Marketing"),
    ("Innvation", "Innvation"),
    ("Others", "Others")
}

INDUSTRIES = {
    (1," "),
    ("FinancialService", "FinancialService"),
    ("HealthCare", "HealthCare"),
    ("ICO", "ICO"),
    ("Others", "Others")
}

# Create your models here.
class Tenant(models.Model):
    db_name = models.CharField(max_length=50, default= None)
    subdomain_prefix = models.CharField(max_length=100, unique=True, default= None)
    company_name = models.CharField(max_length=100, default=None)
    company_email = models.EmailField(max_length=100, unique=True, default= None)
    role = models.CharField(max_length=50, choices=ROLES, default=1)
    country_code = models.IntegerField(default= None)
    mobile_no = models.CharField(max_length=10,default= None)
    industry = models.CharField(max_length=50, choices=INDUSTRIES, default=1)
    website_url = models.CharField(max_length=100, default= None)
    location = models.CharField(max_length=50, default= None)
    additional_info = models.CharField(max_length=120, default= None)
    is_active = models.BooleanField(default= None)
    test_api_token = models.CharField(max_length=100, blank=True, default= None)
    live_api_token = models.CharField(max_length=100, blank=True, default= None)
    sdk_token = models.CharField(max_length=100, blank=True, default= None)
    contact_person = models.CharField(max_length=50, default= None)

    def __str__(self):
        return self.db_name

# class TenantAwareModel(models.Model):
#     tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
#     class Meta:
#         abstract = True
#
#     def __str__(self):
#         return self.tenant