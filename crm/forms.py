from django import forms

from .models import AdvertisingCampaign, Lead, Service


class AdvertisingCampaignForm(forms.ModelForm):

    class Meta:
        model = AdvertisingCampaign
        fields = (
            'name',
            'service',
            'channel',
            'budget',
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
