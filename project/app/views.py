from django.shortcuts import render
from .models import AddProduct
from .forms import AddProductForm
from django.shortcuts import render, get_object_or_404
# Create your views here.
def home(request):
    return render(request,'home.html')


def shop(request):
    return render(request,'shop.html')
def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')
def cart(request):
    return render(request,'cart.html')

def addproduct(request):
    if request.method=="POST":
        form = AddProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        data = AddProduct.objects.all()
        return render(request,'addproduct.html',{'form':form,'data':data})
    form = AddProductForm()
    data = AddProduct.objects.all()
    if data:
        return render(request,'addproduct.html',{'form':form,'data':data})
    else:
        return render(request,'addproduct.html',{'form':form})
    
def addedproduct(request):
        if request.method=="POST":
            form = AddProductForm(request.POST,request.FILES)
            if form.is_valid():
                form.save()
            data = AddProduct.objects.all()
            return render(request,'addedproduct.html',{'form':form,'data':data})
        form = AddProductForm()
        data = AddProduct.objects.all()
        if data:
             return render(request,'addedproduct.html',{'form':form,'data':data})
        else:
             return render(request,'addedproduct.html',{'form':form})
def singlecart(request,pk):
        pdata=get_object_or_404(AddProduct,pk=pk)
        return render(request,'singlecart.html',{'pdata':pdata})
def addtocart(request,pk):
         if request.method == 'POST':
                quantity = request.session.get('quantity', [])
                quantity1 =int(request.POST.get('quantity'))
                quantity.append(quantity1)
                # print("quantity :",quantity)
                request.session['quantity'] = quantity
                cart = request.session.get('cart', [])
                cart.append(pk)
                request.session['cart'] = cart
                form = AddProductForm()
                data = AddProduct.objects.all()
                return render(request,'A',{'form':form,'data':data})
