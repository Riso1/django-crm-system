from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import AdvertisingCampaignForm, LeadForm, ServiceForm
from .models import AdvertisingCampaign, Lead, Service


class ServiceListView(ListView):
    model = Service
    template_name = 'crm/service_list.html'
    context_object_name = 'services'


class ServiceDetailView(DetailView):
    model = Service
    template_name = 'crm/service_detail.html'
    context_object_name = 'service'


class ServiceCreateView(CreateView):
    model = Service
    form_class = ServiceForm
    template_name = 'crm/service_form.html'


class ServiceUpdateView(UpdateView):
    model = Service
    form_class = ServiceForm
    template_name = 'crm/service_form.html'


class ServiceDeleteView(DeleteView):
    model = Service
    template_name = 'crm/service_confirm_delete.html'
    success_url = reverse_lazy('crm:service_list')


class AdvertisingCampaignListView(ListView):
    model = AdvertisingCampaign
    template_name = 'crm/campaign_list.html'
    context_object_name = 'campaigns'


class AdvertisingCampaignDetailView(DetailView):
    model = AdvertisingCampaign
    template_name = 'crm/campaign_detail.html'
    context_object_name = 'campaign'


class AdvertisingCampaignCreateView(CreateView):
    model = AdvertisingCampaign
    form_class = AdvertisingCampaignForm
    template_name = 'crm/campaign_form.html'


class AdvertisingCampaignUpdateView(UpdateView):
    model = AdvertisingCampaign
    form_class = AdvertisingCampaignForm
    template_name = 'crm/campaign_form.html'


class AdvertisingCampaignDeleteView(DeleteView):
    model = AdvertisingCampaign
    template_name = 'crm/campaign_confirm_delete.html'
    success_url = reverse_lazy('crm:campaign_list')


class LeadListView(ListView):
    model = Lead
    template_name = 'crm/lead_list.html'
    context_object_name = 'leads'


class LeadDetailView(DetailView):
    model = Lead
    template_name = 'crm/lead_detail.html'
    context_object_name = 'lead'


class LeadCreateView(CreateView):
    model = Lead
    form_class = LeadForm
    template_name = 'crm/lead_form.html'


class LeadUpdateView(UpdateView):
    model = Lead
    form_class = LeadForm
    template_name = 'crm/lead_form.html'


class LeadDeleteView(DeleteView):
    model = Lead
    template_name = 'crm/lead_confirm_delete.html'
    success_url = reverse_lazy('crm:lead_list')
