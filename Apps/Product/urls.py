from django.urls import path
from .views import (
    DetailListView, DetailCreateView, DetailRetrieveView, DetailUpdateView, DetailDestroyView,
    SummaryDescriptionListView, SummaryDescriptionCreateView, SummaryDescriptionRetrieveView, SummaryDescriptionUpdateView, SummaryDescriptionDestroyView,
    BrandListView, BrandCreateView, BrandRetrieveView, BrandUpdateView, BrandDestroyView,
    CategoryListView, CategoryCreateView, CategoryRetrieveView, CategoryUpdateView, CategoryDestroyView,
    SubCategoryListView, SubCategoryCreateView, SubCategoryRetrieveView, SubCategoryUpdateView, SubCategoryDestroyView,
    PhotosListView, PhotosCreateView, PhotosRetrieveView, PhotosUpdateView, PhotosDestroyView,
    VideosListView, VideosCreateView, VideosRetrieveView, VideosUpdateView, VideosDestroyView,
    ShowRatingListView, ShowRatingCreateView, ShowRatingRetrieveView, ShowRatingUpdateView, ShowRatingDestroyView,
    ReviewListView, ReviewCreateView, ReviewRetrieveView, ReviewUpdateView, ReviewDestroyView,
    InventoryMeterListView, InventoryMeterCreateView, InventoryMeterRetrieveView, InventoryMeterUpdateView, InventoryMeterDestroyView,
    Option1ListView, Option1CreateView, Option1RetrieveView, Option1UpdateView, Option1DestroyView,
    Option2ListView, Option2CreateView, Option2RetrieveView, Option2UpdateView, Option2DestroyView,
    TagsListView, TagsCreateView, TagsRetrieveView, TagsUpdateView, TagsDestroyView,

    )

urlpatterns = [
    path('details/', DetailListView.as_view(), name='detail-list',),
    path('details/create/', DetailCreateView.as_view(), name='detail-create'),
    path('details/retrieve/<int:pk>/', DetailRetrieveView.as_view(), name='detail-retrieve'),
    path('details/update/<int:pk>/', DetailUpdateView.as_view(), name='detail-update'),
    path('details/destroy/<int:pk>/', DetailDestroyView.as_view(), name='detail-destroy'),

    path('summary_description/', SummaryDescriptionListView.as_view(), name='summary-description-list'),
    path('summary_description/create/', SummaryDescriptionCreateView.as_view(), name='summary-description-create'),
    path('summary_description/retrieve/<int:pk>/', SummaryDescriptionRetrieveView.as_view(), name='summary-description-retrieve'),
    path('summary_description/update/<int:pk>/', SummaryDescriptionUpdateView.as_view(), name='summary-description-update'),
    path('summary_description/destroy/<int:pk>/', SummaryDescriptionDestroyView.as_view(), name='summary-description-destroy'),

    path('brand/', BrandListView.as_view(), name='brand-list'),
    path('brand/create/', BrandCreateView.as_view(), name='brand-create'),
    path('brand/retrieve/<int:pk>/', BrandRetrieveView.as_view(), name='brand-retrieve'),
    path('brand/update/<int:pk>/', BrandUpdateView.as_view(), name='brand-update'),
    path('brand/destroy/<int:pk>/', BrandDestroyView.as_view(), name='brand-destroy'),

    path('category/', CategoryListView.as_view(), name='category-list'),
    path('category/create/', CategoryCreateView.as_view(), name='category-create'),
    path('category/retrieve/<int:pk>/',CategoryRetrieveView.as_view(), name='category-retrieve'),
    path('category/update/<int:pk>/', CategoryUpdateView.as_view(), name='category-update'),
    path('category/destroy/<int:pk>/', CategoryDestroyView.as_view(), name='category-destroy'),

    path('sub_category/', SubCategoryListView.as_view(), name='sub-category'),
    path('sub_category/create/', SubCategoryCreateView.as_view(), name='sub-category-create'),
    path('sub-category/retrieve/<int:pk>/', SubCategoryRetrieveView.as_view(), name='sub-category-retrieve'),
    path('sub-category/update/<int:pk>/', SubCategoryUpdateView.as_view(), name='sub-category-update'),
    path('sub-category/destroy/<int:pk>/', SubCategoryDestroyView.as_view(), name='sub-category-destroy'),

    path('photos/', PhotosListView.as_view(), name='photos'),
    path('photos/create/', PhotosCreateView.as_view(), name='photos-create'),
    path('photos/retrieve/<int:pk>/', PhotosRetrieveView.as_view(), name='photos-retrieve'),
    path('photos/update/<int:pk>/', PhotosUpdateView.as_view(), name='photos-update'),
    path('photos/destroy/<int:pk>/', PhotosDestroyView.as_view(), name='photos-destroy'),

    path('videos/', VideosListView.as_view(), name='videos-list'),
    path('videos/create/', VideosCreateView.as_view(), name='videos-create'),
    path('videos/retrieve/<int:pk>/', VideosRetrieveView.as_view(), name='videos-retrieve'),
    path('videos/update/<int:pk>/', VideosUpdateView.as_view(), name='videos-update'),
    path('videos/destroy/<int:pk>/', VideosDestroyView.as_view(), name='videos-destroy'),

    path('show-ratings/', ShowRatingListView.as_view(), name='show-ratings-list'),
    path('show-ratings/create/', ShowRatingCreateView.as_view(), name='show-ratings-create'),
    path('show-ratings/retrieve/<int:pk>/', ShowRatingRetrieveView.as_view(), name='show-ratings-retrieve'),
    path('show-ratings/update/<int:pk>/', ShowRatingUpdateView.as_view(), name='show-ratings-update'),
    path('show-ratings/destroy/<int:pk>/', ShowRatingDestroyView.as_view(), name='show-ratings-destroy'),

    path('review/', ReviewListView.as_view(), name='review-list'),
    path('review/create/', ReviewCreateView.as_view(), name='review-create'),
    path('review/retrieve/<int:pk>/', ReviewRetrieveView.as_view(), name='review-retrieve'),
    path('review/update/<int:pk>/', ReviewUpdateView.as_view(), name='review-update'),
    path('review/destroy/<int:pk>/', ReviewDestroyView.as_view(), name='review-destroy'),

    path('inventory-meter/', InventoryMeterListView.as_view(), name='inventory-meter-list'),
    path('inventory-meter/create/', InventoryMeterCreateView.as_view(), name='inventory-meter-create'),
    path('inventory-meter/retrieve/<int:pk>/', InventoryMeterRetrieveView.as_view(), name='inventory-meter-retrieve'),
    path('inventory-meter/update/<int:pk>/', InventoryMeterUpdateView.as_view(), name='inventory-meter-update'),
    path('inventory-meter/destroy/<int:pk>/', InventoryMeterDestroyView.as_view(), name='inventory-meter-destroy'),

    path('option1/', Option1ListView.as_view(), name='option1-list'),
    path('option1/create/', Option1CreateView.as_view(), name='option1-create'),
    path('option1/retrieve/<int:pk>/', Option1RetrieveView.as_view(), name='option1-retrieve'),
    path('option1/update/<int:pk>/', Option1UpdateView.as_view(), name='option1-update'),
    path('option1/destroy/<int:pk>/', Option1DestroyView.as_view(), name='option1-destroy'),

    path('option2/', Option2ListView.as_view(), name='option2-list'),
    path('option2/create/', Option2CreateView.as_view(), name='option2-create'),
    path('option2/retrieve/<int:pk>/', Option2RetrieveView.as_view(), name='option2-retrieve'),
    path('option2/update/<int:pk>/', Option2UpdateView.as_view(), name='option2-update'),
    path('option2/destroy/<int:pk>/', Option2DestroyView.as_view(), name='option2-destroy'),

    path('tags/', TagsListView.as_view(), name='tags-list'),
    path('tags/create/', TagsCreateView.as_view(), name='tags-create'),
    path('tags/retrieve/<int:pk>/', TagsRetrieveView.as_view(), name='tags-retrieve'),
    path('tags/update/<int:pk>/', TagsUpdateView.as_view(), name='tags-update'),
    path('tags/destroy/<int:pk>/', TagsDestroyView.as_view(), name='tags-destroy')
]
