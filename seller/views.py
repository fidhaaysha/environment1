from django.shortcuts import render

# Create your views here.
def seller_home(request):
    return render(request,'seller/sellerhome.html')

def add_product(request):
    return render(request,'seller/addproducts.html')

def master(request):
        return render(request,'seller/masterpage.html')