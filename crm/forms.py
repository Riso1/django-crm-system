from django import forms

from .models import AdvertisingCampaign, Service


class AdvertisingCampaignForm(forms.ModelForm):

    class Meta:
        model = AdvertisingCampaign
        fields = (
            'name',
            'service',
            'channel',
            'budget',
        )


class ServiceForm(forms.ModelForm):

    class Meta:
        model = Service
        fields = ('name', 'description', 'price')
