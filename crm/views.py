from django.db.models import Count, Sum
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
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
    Service,
)


class ServiceListView(ListView):
    model = Service
    template_name = 'products/products-list.html'
    context_object_name = 'products'


class ServiceDetailView(DetailView):
    model = Service
    template_name = 'products/products-detail.html'
    context_object_name = 'service'


class ServiceCreateView(CreateView):
    model = Service
    form_class = ServiceForm
    template_name = 'products/products-create.html'


class ServiceUpdateView(UpdateView):
    model = Service
    form_class = ServiceForm
    template_name = 'products/products-edit.html'


class ServiceDeleteView(DeleteView):
    model = Service
    template_name = 'products/products-delete.html'
    success_url = reverse_lazy('crm:service_list')


class AdvertisingCampaignListView(ListView):
    model = AdvertisingCampaign
    template_name = 'ads/ads-list.html'
    context_object_name = 'ads'


class AdvertisingCampaignDetailView(DetailView):
    model = AdvertisingCampaign
    template_name = 'ads/ads-detail.html'
    context_object_name = 'campaign'


class AdvertisingCampaignCreateView(CreateView):
    model = AdvertisingCampaign
    form_class = AdvertisingCampaignForm
    template_name = 'ads/ads-create.html'


class AdvertisingCampaignUpdateView(UpdateView):
    model = AdvertisingCampaign
    form_class = AdvertisingCampaignForm
    template_name = 'ads/ads-edit.html'


class AdvertisingCampaignDeleteView(DeleteView):
    model = AdvertisingCampaign
    template_name = 'ads/ads-delete.html'
    success_url = reverse_lazy('crm:campaign_list')


class LeadListView(ListView):
    model = Lead
    template_name = 'leads/leads-list.html'
    context_object_name = 'leads'


class LeadDetailView(DetailView):
    model = Lead
    template_name = 'leads/leads-detail.html'
    context_object_name = 'lead'


class LeadCreateView(CreateView):
    model = Lead
    form_class = LeadForm
    template_name = 'leads/leads-create.html'


class LeadUpdateView(UpdateView):
    model = Lead
    form_class = LeadForm
    template_name = 'leads/leads-edit.html'


class LeadDeleteView(DeleteView):
    model = Lead
    template_name = 'leads/leads-delete.html'
    success_url = reverse_lazy('crm:lead_list')


class ContractListView(ListView):
    model = Contract
    template_name = 'contracts/contracts-list.html'
    context_object_name = 'contracts'


class ContractDetailView(DetailView):
    model = Contract
    template_name = 'contracts/contracts-detail.html'
    context_object_name = 'contract'


class ContractCreateView(CreateView):
    model = Contract
    form_class = ContractForm
    template_name = 'contracts/contracts-create.html'


class ContractUpdateView(UpdateView):
    model = Contract
    form_class = ContractForm
    template_name = 'contracts/contracts-edit.html'


class ContractDeleteView(DeleteView):
    model = Contract
    template_name = 'contracts/contracts-delete.html'
    success_url = reverse_lazy('crm:contract_list')


class CustomerListView(ListView):
    model = Customer
    template_name = 'customers/customers-list.html'
    context_object_name = 'customers'


class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'customers/customers-detail.html'
    context_object_name = 'customer'


class CustomerUpdateView(UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customers/customers-edit.html'


class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'customers/customers-delete.html'
    success_url = reverse_lazy('crm:customer_list')


class CustomerCreateView(CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customers/customers-create.html'

    def get_initial(self):
        initial = super().get_initial()
        lead = get_object_or_404(Lead, pk=self.kwargs['lead_pk'])
        initial['lead'] = lead
        return initial


class CampaignStatsView(ListView):
    model = AdvertisingCampaign
    template_name = 'ads/ads-statistic.html'
    context_object_name = 'ads'

    def get_queryset(self):
        campaigns = AdvertisingCampaign.objects.annotate(
            leads_count=Count('leads', distinct=True),
            customers_count=Count('leads__customer', distinct=True),
            income=Sum('leads__customer__contract__amount'),
        )

        for campaign in campaigns:
            income = campaign.income or 0
            campaign.profit = income - campaign.budget

        return campaigns
