from django.shortcuts import render
from .models import AddProduct,Details
from .forms import AddProductForm
from django.shortcuts import render,redirect
from django.shortcuts import render, get_object_or_404
from project.settings import MEDIA_ROOT,MEDIA_URL
import razorpay
from django.views.decorators.csrf import csrf_exempt
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

    return redirect('addedproduct') 
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




# def deletecart(request,pk):
#     cart = request.session.get('cart',[])
#     quantity = request.session.get('quantity',[])
#     print("Cart :",cart)
#     print("Quantity :",quantity)
#     print("pk=",pk)
#     x = cart.index(pk)
#     # print("Cart index no:",x)
#     # y = quantity[x]
#     # print("Quantity of that card index:",y)
#     cart1=[]
#     y = len(cart)   
#     i=0
#     while i<y:
#         if i==x:
#             pass
#         else:
#             cart1.append(cart[i])
#         i+=1
#     print(cart1)
#     request.session['cart']=cart1
#     quantity1=[]
#     z = len(quantity)
#     j=0
#     while j<z:
#         if j==x:
#             pass
#         else:
#             quantity1.append(quantity[j])
#         j+=1
#     print(quantity1)
#     request.session['quantity']=quantity1
#     # ----------------------------------------------------
#     cart = request.session.get('cart',[])
#     quantity = request.session.get('quantity',[])
#     print("Cart :",cart)
#     print("Quantity :",quantity)
#     # print(len(cart))
#     alldata = []
#     i=0
#     j=0
#     total=0
    
#     while i < len(cart):
#         data = AddProduct.objects.get(id=cart[i])
#         # print(quantity[j])
#         total = total + (data.Product_price)*1
#         # print(data.id)
#         # print(data.iten_name)
#         # print(data.item_desc)
#         # print(data.item_price)
#         # print(data.item_image)
#         alldata.append({
#                 'id':data.id,
#                 'Product_name':data.Product_name,
#                 'Product_descip':data.Product_descip,
#                 'Product_price':data.Product_price,
#                 'Product_image':data.Product_image,
#             })
#         ami=len(alldata)
#         i+=1
#         j+=1
#     # print("Total Amount = ",total)
#     print(alldata)
#     return render(request,'cart.html',{'key':alldata,'amount':total,'ami':ami})
def checkout(request):
    return render(request,'checkout.html')

def payment(request):
    global payment
    if request.method=="POST":
        # amount in paisa
        # amount = request.POST.get('total') * 100
        cart = request.session.get('cart',[])

        i=0
        j=0
        total=0
        while i < len(cart):
            data = AddProduct.objects.get(id=cart[i])
        # print(quantity[j])
            total = total + (data.Product_price)*1
        amount=total*100
        client = razorpay.Client(auth =("rzp_test_92mue1NgSEbYJU" , "FKY3qexqw91YDDJCBVCFWJXA"))
        # create order
        
        data = { "amount": amount, "currency": "INR", "receipt": "order_rcptid_11" }
        payment = client.order.create(data=data)
        product = Details.objects.create( amount =amount , order_id = payment['id'])
        cart = request.session.get('cart',[])
        quantity = request.session.get('quantity',[])
        # amount = request.POST.get('amount') * 100

        alldata = []
        i=0
        j=0
        total=0
        while i < len(cart):
            data = AddProduct.objects.get(id=cart[i])
            total = total + (data.Product_price)*1
            alldata.append({
                'id':data.id,
                'Product_name':data.Product_name,
                'Product_descip':data.Product_descip,
                'Product_price':data.Product_price,
                'Product_image':data.Product_image,
            })
            i+=1
            j+=1
        # print(payment)
        return render(request,'shop.html',{'key':alldata,'amount':total,'payment':payment})
@csrf_exempt
def payment_status(request):
       if request.method=="POST": 
        response = request.POST
        print(response) #  
        print(payment)

        razorpay_data = {
            'razorpay_order_id': response['razorpay_order_id'],
            'razorpay_payment_id': response['razorpay_payment_id'],
            'razorpay_signature': response['razorpay_signature']
        }

        # client instance
        client = razorpay.Client(auth =("rzp_test_92mue1NgSEbYJU" , "FKY3qexqw91YDDJCBVCFWJXA"))

        try:
            status = client.utility.verify_payment_signature(razorpay_data)
            product = Details.objects.get(order_id=response['razorpay_order_id'])
            product.razorpay_payment_id = response ['razorpay_payment_id']
            product.paid = True
            product.save()
            
            # return redirect('home')
            return render(request, 'home.html', {'status': True})
        except:
            # return redirect('home')

            return render(request, 'home.html', {'status': False})
def deletecart(request,pk):
    cart = request.session.get('cart',[])
    quantity = request.session.get('quantity',[])
    print("Cart :",cart)
    print("Quantity :",quantity)
    print("pk=",pk)
    x = cart.index(pk)
    # print("Cart index no:",x)
    # y = quantity[x]
    # print("Quantity of that card index:",y)
    cart1=[]
    y = len(cart)   
    i=0
    while i<y:
        if i==x:
            pass
        else:
            cart1.append(cart[i])
        i+=1
    print(cart1)
    request.session['cart']=cart1
    quantity1=[]
    z = len(quantity)
    j=0
    while j<z:
        if j==x:
            pass
        else:
            quantity1.append(quantity[j])
        j+=1
    print(quantity1)
    request.session['quantity']=quantity1
    # ----------------------------------------------------
    cart = request.session.get('cart',[])
    quantity = request.session.get('quantity',[])
    print("Cart :",cart)
    print("Quantity :",quantity)
    # print(len(cart))
    alldata = []
    i=0
    j=0
    total=0
    while i < len(cart):
        data = AddProduct.objects.get(id=cart[i])
        print(quantity[j])
        total = total + (data.item_price)*quantity[j]
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
    print(alldata)
    return render(request,'app/cart.html',{'key':alldata,'amount':total})
def register(request):
    return render(request,'register.html')
