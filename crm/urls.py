from django.urls import path

from .views import (
    AdvertisingCampaignCreateView,
    AdvertisingCampaignDeleteView,
    AdvertisingCampaignDetailView,
    AdvertisingCampaignListView,
    AdvertisingCampaignUpdateView,
    CampaignStatsView,
    ContractCreateView,
    ContractDeleteView,
    ContractDetailView,
    ContractListView,
    ContractUpdateView,
    CustomerCreateView,
    CustomerDeleteView,
    CustomerDetailView,
    CustomerListView,
    CustomerUpdateView,
    LeadCreateView,
    LeadDeleteView,
    LeadDetailView,
    LeadListView,
    LeadUpdateView,
    ServiceCreateView,
    ServiceDeleteView,
    ServiceDetailView,
    ServiceListView,
    ServiceUpdateView,
)

app_name = 'crm'

urlpatterns = [
    path('', ServiceListView.as_view(), name='home'),

    path('products/', ServiceListView.as_view(), name='service_list'),
    path('products/new', ServiceCreateView.as_view(), name='service_create'),
    path('products/<int:pk>/', ServiceDetailView.as_view(), name='service_detail'),
    path('products/<int:pk>/edit', ServiceUpdateView.as_view(), name='service_update'),
    path('products/<int:pk>/delete', ServiceDeleteView.as_view(), name='service_delete'),

    path('ads/', AdvertisingCampaignListView.as_view(), name='campaign_list'),
    path('ads/new', AdvertisingCampaignCreateView.as_view(), name='campaign_create'),
    path('ads/<int:pk>/', AdvertisingCampaignDetailView.as_view(), name='campaign_detail'),
    path('ads/<int:pk>/edit', AdvertisingCampaignUpdateView.as_view(), name='campaign_update'),
    path('ads/<int:pk>/delete', AdvertisingCampaignDeleteView.as_view(), name='campaign_delete'),
    path('ads/statistic/', CampaignStatsView.as_view(), name='campaign_stats'),

    path('leads/', LeadListView.as_view(), name='lead_list'),
    path('leads/new', LeadCreateView.as_view(), name='lead_create'),
    path('leads/<int:pk>/', LeadDetailView.as_view(), name='lead_detail'),
    path('leads/<int:lead_pk>/convert/', CustomerCreateView.as_view(), name='customer_create'),
    path('leads/<int:pk>/edit', LeadUpdateView.as_view(), name='lead_update'),
    path('leads/<int:pk>/delete', LeadDeleteView.as_view(), name='lead_delete'),

    path('contracts/', ContractListView.as_view(), name='contract_list'),
    path('contracts/new', ContractCreateView.as_view(), name='contract_create'),
    path('contracts/<int:pk>/', ContractDetailView.as_view(), name='contract_detail'),
    path('contracts/<int:pk>/edit', ContractUpdateView.as_view(), name='contract_update'),
    path('contracts/<int:pk>/delete', ContractDeleteView.as_view(), name='contract_delete'),

    path('customers/', CustomerListView.as_view(), name='customer_list'),
    path('customers/<int:pk>/', CustomerDetailView.as_view(), name='customer_detail'),
    path('customers/<int:pk>/edit', CustomerUpdateView.as_view(), name='customer_update'),
    path('customers/<int:pk>/delete', CustomerDeleteView.as_view(), name='customer_delete'),
]