from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import (
    SnippetList,
    ItemDetails,
    GenericAPIView,
    ItemViewSet,
)

from .views import (
    HomeView,
    ItemDetailView,
    OrderSummaryView,
    add_to_cart,
    remove_from_cart,
    remove_single_item_from_cart,
)

app_name = 'core'


router = DefaultRouter()
router.register('item', ItemViewSet, basename='item')

urlpatterns = [
    #views
    path('', HomeView.as_view(), name='home'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,
         name='remove-single-item-from-cart'),

    #api
    path('api-root/', include(router.urls)),
    path('add/', SnippetList.as_view()),
    path('item/<int:id>/', ItemDetails.as_view()),
    path('Generic/', GenericAPIView.as_view()),
]
