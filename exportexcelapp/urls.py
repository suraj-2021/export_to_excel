from django.urls import path
from.views import export_to_excel, add_products

urlpatterns = [

    path('export/', export_to_excel, name='csv-export'),
    path('add_products',add_products,name='add-products'),
]