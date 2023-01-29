from django.contrib import admin
from .models import product
from django.contrib.auth.models import Group
# Register your models here.
class productadmin(admin.ModelAdmin):
    list_display=('name','price','description','image')


admin.site.register(product,productadmin)

# class MyAdminSite(admin.AdminSite):
#     admin_header="cryptomining"

admin.site.unregister(Group)


admin.site.site_header="INDIAN CRYPTO MINING"
admin.site.site_title="welcome admin"



# list filter 
# list_filter=('price', )