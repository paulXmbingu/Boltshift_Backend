from django.urls import path
from .views import (
    DetailListView, DetailCreateView, DetailRetrieveView, DetailUpdateView, DetailDestroyView,
    
    )


urlpatterns = [
    # DETAIL URLS
    path('details/', DetailListView.as_view(), name='detail-list',),
    path('details/create/', DetailCreateView.as_view(), name='detail-create'),
    path('details/retrieve/<int:pk>/', DetailRetrieveView.as_view(), name='detail-retrieve'),
    path('details/update/<int:pk>/', DetailUpdateView.as_view(), name='detail-update'),
    path('details/destroy/<int:pk>/', DetailDestroyView.as_view(), name='detail-destroy'),
]
