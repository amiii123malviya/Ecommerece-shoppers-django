from django.shortcuts import render
from .models import AddProduct
from .forms import AddProductForm
from django.shortcuts import render,redirect
from django.shortcuts import render, get_object_or_404
from project.settings import MEDIA_ROOT,MEDIA_URL
# Create your views here.
def home(request):
    return render(request,'home.html')


def shop(request):
    return render(request,'shop.html')
def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

    

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
# def singlecart(request,pk):
#         if request.method == 'POST':
#             pdata=get_object_or_404(AddProduct,pk=pk)
#         return render(request,'singlecart.html',{'pdata':pdata})
def addtocart(request,pk):
    product = get_object_or_404(AddProduct, id=pk)
    cart = request.session.get('cart', [])
    quantities = request.session.get('quantities', [])

    if pk in cart:
        index = cart.index(pk)
        if index < len(quantities):
            quantities[index] += 1
            print(quantities)
        else:
            print("Error: Cart and quantities list are out of sync.")
            quantities.append(1)  # Fix by adding a new entry for consistency
    else:
        cart.append(pk)
        quantities.append(1)

    request.session['cart'] = cart
    print(cart)
    request.session['quantities'] = quantities
    print(quantities)

    request.session['added_to_cart'] = True

    return redirect('cart') 
from django.shortcuts import render

def cart(request):
        cart = request.session.get('cart',[])
        quantity = request.session.get('quantity',[])
    # print("Cart :",cart)
    # print("Quantity :",quantity)
    # print(len(cart))
        alldata = []
        i=0
        j=0
        total=0
        while i < len(cart):
            data = AddProduct.objects.get(id=cart[i])
            # print(quantity[j])
            total = total + (data.Product_price)*1
        # print(data.id)
        # print(data.iten_name)
        # print(data.item_desc)
        # print(data.item_price)
        # print(data.item_image)
            alldata.append({
                'id':data.id,
                'Product_name':data.Product_name,
                'Product_descip':data.Product_descip,
                'Product_price':data.Product_price,
                'Product_image':data.Product_image,
            })
            i+=1
            j+=1
    # print("Total Amount = ",total)
    # print(alldata)
        return render(request,'cart.html',{'key':alldata,'amount':total})
    #-------------------------------------

    # # Example data fetching, you need to replace it with your actual data retrieval logic
    # data = [
    #     {"Product_price": 10},
    #     {"Product_price": None},
    #     {"Product_price": 20}
    # ]
    # quantities = [1, None, 2]

    # cart_items = []
    # total = 0

    # min_length = min(len(data), len(quantities))  # Ensure we only iterate up to the length of the shortest list

    # for j in range(min_length):
    #     product_price = data[j].get('Product_price')
    #     qty = quantities[j]

    #     if product_price is None or qty is None:
    #         continue  # Skip items with None values

    #     item_total = product_price * qty
    #     total += item_total
    #     cart_items.append({
    #         'product_price': product_price,
    #         'quantity': qty,
    #         'item_total': item_total
    #     })

    # context = {
    #     'cart_items': cart_items,
    #     'total': total
    # }

    # return render(request, 'cart.html', context)
