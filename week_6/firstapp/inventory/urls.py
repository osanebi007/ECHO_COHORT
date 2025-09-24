from django.urls import path  
from .views import get_product, post_product, update_product, patch_product, delete_product
urlpatterns = [
    path('getproduct/', get_product),
    path('postproduct/', post_product),        
    path('updateproduct/<int:index>/', update_product),
    path('deleteproduct/<int:index>/', delete_product),
    path('patchproduct/<int:index>/', patch_product)
]