from django.shortcuts import redirect, render
from django.http import HttpResponse
from openpyxl import Workbook
from .models import Product
from .forms import ProductForm

def export_to_excel(request):
    response = HttpResponse(content_type = 'application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename ="products.xlsx"'

    wb = Workbook()
    ws = wb.active
    ws.title = "Products"

    #add headers
    headers = ["name","Price","quantity"]
    ws.append(headers)

    #add products
    products = Product.objects.all()
    for product in products:
        ws.append([product.name,product.price,product.quantity])
    #save the workbook to the HttpRespose
    wb.save(response)
    return response

def add_products(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add-products')
    else:
        form = ProductForm()
    return render (request,'add_products.html',{'form':form})