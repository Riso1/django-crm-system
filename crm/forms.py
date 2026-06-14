from django import forms

from .models import (
    AdvertisingCampaign,
    Contract,
    Customer,
    Lead,
    Service
)


class AdvertisingCampaignForm(forms.ModelForm):

    class Meta:
        model = AdvertisingCampaign
        fields = (
            'name',
            'service',
            'channel',
            'budget',
        )


class ContractForm(forms.ModelForm):

    class Meta:
        model = Contract
        fields = (
            'name',
            'service',
            'document',
            'signed_at',
            'valid_until',
            'amount',
        )


class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = (
            'lead',
            'contract',
        )


class LeadForm(forms.ModelForm):

    class Meta:
        model = Lead
        fields = (
            'full_name',
            'phone',
            'email',
            'campaign',
        )


class ServiceForm(forms.ModelForm):

    class Meta:
        model = Service
        fields = ('name', 'description', 'price')
