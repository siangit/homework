from django.contrib import admin
from addresses.models import Address

# Register your models here.
@admin.register(Address)
class UsersAdmin(admin.ModelAdmin):
		list_display = ('user','street','city','state','postal_code','country')
		list_filter = ('city','state','country')
		search_fields = ('user_name','street','postal_code','city','state')
