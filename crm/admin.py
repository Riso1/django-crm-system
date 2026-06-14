from django.contrib import admin

from .models import (
    AdvertisingCampaign,
    Contract,
    Customer,
    Lead,
    Service,
)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')
    search_fields = ('name',)


@admin.register(AdvertisingCampaign)
class AdvertisingCampaignAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'service', 'channel', 'budget')
    list_filter = ('channel',)
    search_fields = ('name', 'channel')


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'phone', 'email', 'campaign')
    list_filter = ('campaign',)
    search_fields = ('full_name', 'phone', 'email')


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'service', 'signed_at', 'valid_until', 'amount')
    list_filter = ('service', 'signed_at')
    search_fields = ('name',)


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'lead', 'contract')
    search_fields = ('lead__full_name', 'contract__name')