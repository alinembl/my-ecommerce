from django.shortcuts import render, redirect
from .models import Product
# Create your views here.



def cartItems(cart):
	items =[]
	for item in cart:
		items.append(Product.objects.get(id=int(item)))
	return items

def genItemsList(cart):
	cart_items = cartItems(cart)
	item_list = ""
	for item in cart_items:
		item_list += srt(item.name)
		item_list += ","
	return item_list

def priceCart(cart):
	cart_items = cartItems(cart)
	price = 0
	for item in cart_items:
		price+= item.price
	return price

def catalog(request):
	if 'cart' not in request.session:
		request.session['cart'] = []
	cart = request.session['cart']
	request.session.set_expiry(0)
	store_items = Product.objects.all()
	ctx = {'store_items': store_items,'cart_size':len(cart)}
	
	if request.method =="POST":
		cart.append(int(request.POST['obj_id']))
		return redirect('catalog')
	
	return render(request,'store/catalog.html',ctx)

def cart(request):
	cart = request.session['cart']
	request.session.set_expiry(0)
	ctx = {'cart': cart, 'cart_size':len(cart),'cart_items':cartItems(cart),'total_price':priceCart(cart)}
	return render(request,"store/cart.html",ctx)

def removefromcart(request):
    request.session.set_expiry(0)
    obj_to_remove = int(request.POST['obj_id'])
    obj_index = request.session['cart'].index(obj_to_remove)
    request.session['cart'].pop(obj_index)
    return redirect("cart")

def checkout(request):
	request.session.set_expiry(0)
	cart = request.session['cart']
	ctx = {'cart': cart, 'cart_size':len(cart),'total_price':priceCart(cart)}
	return render(request, "store/checkout.html")

def completeOrder(request):
	request.session.set_expiry(0)
	cart = request.session['cart']
	order = Order()
	order.first_name = request.POST['first_name']
	order.last_name = request.POST['last_name']
	order.adress = request.POST['adress']
	order.city = request.POST['city']
	order.payment_method = request.POST['payment']
	order.payment_data = request.POST['payment_data']
	order.items = genItemsList(cart)
	request.session['cart'] = []
	return render(request,"store/complete_order.html",None)
