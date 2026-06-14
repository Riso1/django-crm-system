from django.urls import path

from .views import (
    AdvertisingCampaignCreateView,
    AdvertisingCampaignDeleteView,
    AdvertisingCampaignDetailView,
    AdvertisingCampaignListView,
    AdvertisingCampaignUpdateView,
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
    CampaignStatsView,
)

app_name = 'crm'

urlpatterns = [
    path('services/', ServiceListView.as_view(), name='service_list'),
    path('services/create/', ServiceCreateView.as_view(), name='service_create'),
    path('services/<int:pk>/', ServiceDetailView.as_view(), name='service_detail'),
    path('services/<int:pk>/update/', ServiceUpdateView.as_view(), name='service_update'),
    path('services/<int:pk>/delete/', ServiceDeleteView.as_view(), name='service_delete'),

    path('ads/', AdvertisingCampaignListView.as_view(), name='campaign_list'),
    path('ads/create/', AdvertisingCampaignCreateView.as_view(), name='campaign_create'),
    path('ads/<int:pk>/', AdvertisingCampaignDetailView.as_view(), name='campaign_detail'),
    path('ads/<int:pk>/update/', AdvertisingCampaignUpdateView.as_view(), name='campaign_update'),
    path('ads/<int:pk>/delete/', AdvertisingCampaignDeleteView.as_view(), name='campaign_delete'),

    path('leads/', LeadListView.as_view(), name='lead_list'),
    path('leads/create/', LeadCreateView.as_view(), name='lead_create'),
    path('leads/<int:pk>/', LeadDetailView.as_view(), name='lead_detail'),
    path('leads/<int:lead_pk>/convert/', CustomerCreateView.as_view(), name='customer_create'),
    path('leads/<int:pk>/update/', LeadUpdateView.as_view(), name='lead_update'),
    path('leads/<int:pk>/delete/', LeadDeleteView.as_view(), name='lead_delete'),

    path('contracts/', ContractListView.as_view(), name='contract_list'),
    path('contracts/create/', ContractCreateView.as_view(), name='contract_create'),
    path('contracts/<int:pk>/', ContractDetailView.as_view(), name='contract_detail'),
    path('contracts/<int:pk>/update/', ContractUpdateView.as_view(), name='contract_update'),
    path('contracts/<int:pk>/delete/', ContractDeleteView.as_view(), name='contract_delete'),

    path('customers/', CustomerListView.as_view(), name='customer_list'),
    path('customers/<int:pk>/', CustomerDetailView.as_view(), name='customer_detail'),
    path('customers/<int:pk>/update/', CustomerUpdateView.as_view(), name='customer_update'),
    path('customers/<int:pk>/delete/', CustomerDeleteView.as_view(), name='customer_delete'),

    path('stats/', CampaignStatsView.as_view(), name='campaign_stats'),
]
