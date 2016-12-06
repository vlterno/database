from django.shortcuts import render
from .models import Pc, Notebook, Smartphone, Product

def devicedb_list(request):
	pcs = Pc.objects.order_by("model_name")
	notebooks = Notebook.objects.order_by("model_name")
	smartphones = Smartphone.objects.order_by("model_name")
	products = Product.objects.order_by("model_name")
	return render(request, 'devicedb/devicedb_list.html', {
		'pcs': pcs, 
		'notebooks': notebooks, 
		'smartphones': smartphones, 
		'products': products
	})