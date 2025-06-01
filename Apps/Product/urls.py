from django.urls import path
from .views import (DetailModelListView, DetailModelCreateView, DetailModelRetrieveView, DetailModelUpdateView, DetailModelDestroyView,)

urlpatterns = [
    path('details/', DetailModelListView.as_view(), name='detail_list'),
    path('details/create/', DetailModelCreateView.as_view(), name='detail_create'),
    path('details/<int:pk>/', DetailModelRetrieveView.as_view(), name='detail_retrieve'),
    path('details/<int:pk>/update/', DetailModelUpdateView.as_view(), name='detail_update'),
    path('details/<int:pk>/delete/', DetailModelDestroyView.as_view(), name='detail_delete'),
]
