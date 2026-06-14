from django.urls import path

from .views import (
    ServiceCreateView,
    ServiceDeleteView,
    ServiceDetailView,
    ServiceListView,
    ServiceUpdateView,
)

app_name = 'crm'

urlpatterns = [
    path(
        'services/',
        ServiceListView.as_view(),
        name='service_list'
    ),

    path(
        'services/create/',
        ServiceCreateView.as_view(),
        name='service_create'
    ),

    path(
        'services/<int:pk>/',
        ServiceDetailView.as_view(),
        name='service_detail'
    ),

    path(
        'services/<int:pk>/update/',
        ServiceUpdateView.as_view(),
        name='service_update'
    ),

    path(
        'services/<int:pk>/delete/',
        ServiceDeleteView.as_view(),
        name='service_delete'
    ),
]