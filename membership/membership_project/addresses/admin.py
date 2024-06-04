from django.contrib import admin
from .models import Address

@admin.register(Address)
class AddressesAdmin(admin.ModelAdmin):
    #코드 작성
    list_display = ["user", "street", "city", "state", "postal_code","country"]
    list_filter = ["city", "state","country"]
    search_fields = ["user", "street","postal_code", "city","state"]