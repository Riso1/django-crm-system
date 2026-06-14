from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import (
    AdvertisingCampaignForm,
    ContractForm,
    CustomerForm,
    LeadForm,
    ServiceForm,
)
from .models import (
    AdvertisingCampaign,
    Contract,
    Customer,
    Lead,
    Service
)


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


class ContractListView(ListView):
    model = Contract
    template_name = 'crm/contract_list.html'
    context_object_name = 'contracts'


class ContractDetailView(DetailView):
    model = Contract
    template_name = 'crm/contract_detail.html'
    context_object_name = 'contract'


class ContractCreateView(CreateView):
    model = Contract
    form_class = ContractForm
    template_name = 'crm/contract_form.html'


class ContractUpdateView(UpdateView):
    model = Contract
    form_class = ContractForm
    template_name = 'crm/contract_form.html'


class ContractDeleteView(DeleteView):
    model = Contract
    template_name = 'crm/contract_confirm_delete.html'
    success_url = reverse_lazy('crm:contract_list')


class CustomerListView(ListView):
    model = Customer
    template_name = 'crm/customer_list.html'
    context_object_name = 'customers'


class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'crm/customer_detail.html'
    context_object_name = 'customer'


class CustomerUpdateView(UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'crm/customer_form.html'


class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'crm/customer_confirm_delete.html'
    success_url = reverse_lazy('crm:customer_list')


class CustomerCreateView(CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'crm/customer_form.html'

    def get_initial(self):
        initial = super().get_initial()

        lead = get_object_or_404(
            Lead,
            pk=self.kwargs['lead_pk'],
        )

        initial['lead'] = lead

        return initial
