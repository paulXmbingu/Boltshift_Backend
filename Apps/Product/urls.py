from django.urls import path
from .views import (
    DetailListView, DetailCreateView, DetailRetrieveView, DetailUpdateView, DetailDestroyView,
    SummaryDescriptionListView, SummaryDescriptionCreateView, SummaryDescriptionRetrieveView, SummaryDescriptionUpdateView, SummaryDescriptionDestroyView,

    )


urlpatterns = [
    # DETAIL URLS
    path('details/', DetailListView.as_view(), name='detail-list',),
    path('details/create/', DetailCreateView.as_view(), name='detail-create'),
    path('details/retrieve/<int:pk>/', DetailRetrieveView.as_view(), name='detail-retrieve'),
    path('details/update/<int:pk>/', DetailUpdateView.as_view(), name='detail-update'),
    path('details/destroy/<int:pk>/', DetailDestroyView.as_view(), name='detail-destroy'),

    # SUMMARY DESCRIPTION URLS
    path('summary_description/', SummaryDescriptionListView.as_view(), name='summary-description-list'),
    path('summary_description/create/', SummaryDescriptionCreateView.as_view(), name='summary-description-create'),
    path('summary_description/retrieve/<int:pk>/', SummaryDescriptionRetrieveView.as_view(), name='summary-description-retrieve'),
    path('summary_description/update/<int:pk>/', SummaryDescriptionUpdateView.as_view(), name='summary-description-update'),
    path('summary_description/destroy/<int:pk>/', SummaryDescriptionDestroyView.as_view(), name='summary-description-destroy')
]
