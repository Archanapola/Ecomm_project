from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views import View
from django.db.models import Count
from django.db.models import Q
import razorpay

from accounts.forms import RegistrationForm, ProfileForm
from django.conf import settings
from .models import Cart, Order, Payment, Product, Customer, Wishlist
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.

@login_required
def home(request):
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user =request.user))
        wishitem = len(Wishlist.objects.filter(user = request.user))
    return render(request, 'app/home.html', locals())

@method_decorator(login_required, name='dispatch')
class CategoryView(View):
    def get(self, request, val):
        totalitem = 0
        wishitem = 0


        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user =request.user))
            wishitem = len(Wishlist.objects.filter(user = request.user))

        product = Product.objects.filter(category=val)
        title = Product.objects.filter(category = val).values('title').annotate(total=Count('title'))
        return render(request, "app/category.html", locals())
    
@method_decorator(login_required, name='dispatch')
class CategoryTitleView(View):
    def get(self, request, val):
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user =request.user))
            wishitem = len(Wishlist.objects.filter(user = request.user))

        product = Product.objects.filter(title=val)   
        title = Product.objects.filter(category=product[0].category).values('title')
        return render(request, "app/category.html", locals())


@method_decorator(login_required, name='dispatch')
class ProductDetailsView(View):
    def get(self,request,pk):
        product = Product.objects.get(pk=pk)
        wishlist = Wishlist.objects.filter(Q(product=product)& Q(user=request.user))
        
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user =request.user))
            wishitem = len(Wishlist.objects.filter(user = request.user))


        return render(request, 'app/productdetails.html', locals())
@method_decorator(login_required, name='dispatch')
class AboutUsView(View):
    def get(self,request):
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user =request.user))
            wishitem = len(Wishlist.objects.filter(user = request.user))

        return render(request, 'app/aboutus.html', locals())
@method_decorator(login_required, name='dispatch')
class ContactUsView(View):
    def get(self,request):
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user =request.user))
            wishitem = len(Wishlist.objects.filter(user = request.user))

        return render(request, 'app/contactus.html', locals())




""" query = request.GET.get('q')  # Get search query from request
    products = Product.objects.all()

    # Filter products based on the category field if a query exists
    if query:
        products = products.filter(category__icontains=query)

    context = {
        'products': products,
        'query': query,
    } """
@login_required
def search(request):
    query = request.GET['search']
    if query:
        product = Product.objects.filter(title__icontains=query)
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user =request.user))
        wishitem = len(Wishlist.objects.filter(user = request.user))
    return render(request, 'app/search.html', locals())

@method_decorator(login_required, name='dispatch')
class BuyNowView(View):
    def get(self,request,pk):
        return render(request, 'app/buynow.html', locals())


class RegistrationView(View):
    def get(self, request):
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user =request.user))
            wishitem = len(Wishlist.objects.filter(user = request.user))

        form = RegistrationForm()
        return render(request, 'app/registration.html', locals())
    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful! You can now log in.")
        else:
            messages.warning(request, "Invalid Input Data")
        return render(request, 'app/registration.html', locals())








def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)  # Log the user in
            messages.success(request, "Login successful! Welcome back.")
            return redirect(' ')  # Redirect to the home page or dashboard
        else:
            messages.error(request, "Invalid email or password.")
            return redirect('login')  # Redirect back to the login page

    return render(request, 'app/login.html')  # Render login form



# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib import messages
from .forms import AddressForm, PasswordResetForm, ProfileForm
from .models import Customer
@method_decorator(login_required, name='dispatch')
class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user =request.user))
            wishitem = len(Wishlist.objects.filter(user = request.user))

        form = ProfileForm
        return render(request, 'app/profile.html', locals())

    # Handle POST request
    def post(self, request):
        form = ProfileForm(request.POST)
        if form.is_valid():
            user = request.user

            name = form.cleaned_data['name']

            mobile = form.cleaned_data['mobile']

            city = form.cleaned_data['city']

            state = form.cleaned_data['state']

            zipcode = form.cleaned_data['zipcode']
            
            reg = Customer(user=user, name=name, mobile=mobile, city=city,state=state, zipcode=zipcode)
            reg.save()
            messages.success(request, 'Your profile has been updated successfully!')
        else:
            messages.warning(request, 'Invalid Input')

        return render(request,'app/profile.html', locals())





@login_required
def AddressView(request):
    add = Customer.objects.filter(user=request.user)
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user =request.user))
        wishitem = len(Wishlist.objects.filter(user = request.user))

    return render(request, 'app/address.html', locals())

"""    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            # Save the new address and associate it with the current user
            new_address = form.save(commit=False)
            new_address.user = request.user  # Assign the logged-in user to the new address
            new_address.save()
            messages.success(request, 'New address added successfully!')
            return redirect('address_list_create')  # Refresh the page to show the new address
    else:
        form = AddressForm()"""


@method_decorator(login_required, name='dispatch')
class UpdatAddressView(View):
    def get(self, request, pk):
        totalitem = 0
        wishitem = 0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user =request.user))
            wishitem = len(Wishlist.objects.filter(user = request.user))

        add = Customer.objects.get(pk=pk)
        form = ProfileForm(instance=add)
        return render(request,'app/updateAddress.html', locals() )
    def post(self, request, pk):
        form = ProfileForm(request.POST)
        if form.is_valid():
            add = Customer.objects.get(pk=pk)

            add.name = form.cleaned_data['name']

            add.mobile = form.cleaned_data['mobile']

            add.city = form.cleaned_data['city']

            add.state = form.cleaned_data['state']

            add.zipcode = form.cleaned_data['zipcode']
            
            add.save()
            messages.success(request, 'Your address has been updated successfully!')
        else:
            messages.warning(request, 'Invalid Input')
        return redirect("address")



@login_required
def add_to_cart(request,pk):
    user = request.user
    #product_id = request.GET.get('prod_id')
    product = Product.objects.get(pk=pk)
    Cart(user=user, product=product).save()
    return redirect('/cart')

@login_required
def show_cart(request):
    user = request.user
    cart = Cart.objects.filter(user=user)
    amount = 0 
    for p in cart:
        value = p.quantity*p.product.discounted_price
        amount  = value + amount
    totalamount = amount + 40

    totalitem = 0
    wishitem =0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user =request.user))
        wishitem = len(Wishlist.objects.filter(user = request.user))


    return render(request, 'app/addtocart.html', locals())

@login_required
def show_wishlist(request):
    user = request.user
   
    totalitem = 0
    wishitem =0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user =request.user))
        wishitem = len(Wishlist.objects.filter(user = request.user))

    product = Wishlist.objects.filter(user=user)
    return render(request, 'app/wishlist.html', locals())

@method_decorator(login_required, name='dispatch')
class checkout(View):
    def get(self, request):
        totalitem = 0
        wishitem =0
        if request.user.is_authenticated:
            totalitem = len(Cart.objects.filter(user =request.user))
            wishitem = len(Wishlist.objects.filter(user = request.user))


        user = request.user
        add = Customer.objects.filter(user=user)
        cart_items = Cart.objects.filter(user=user)
        tamount = 0
        for p in cart_items:
            value = p.quantity * p.product.discounted_price
            tamount = value + tamount
        totalamount = tamount + 40

        razoramount = int(totalamount*100)
        client = razorpay.Client(auth= (settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))

        data = {"amount":razoramount, "currency":"INR", "receipt":"order_receiptid_12"}
        payment_response = client.order.create(data= data)
        print(payment_response)

        order_id = payment_response['id']
        order_status = payment_response['status']
        if order_status == 'created':
            payment = Payment(
                user=user,
                amount = razoramount,
                razorpay_order_id = order_id,
                razorpay_payment_status = order_status
            )
            payment.save()
        return render(request, 'app/checkout.html', locals())
    
@login_required
def payment_done(request):
    order_id = request.GET.get('order_id')
    print("order iddd ")
    payment_id = request.GET.get('payment_id')
    print("payment_id iddd " )

    cust_id = request.GET.get('cust_id')
    print("cust_id iddd " )


    user = request.user 

    customer = Customer.objects.get(id=cust_id)

    payment = Payment.objects.get(razorpay_order_id = order_id)
    payment.paid=True
    payment.razorpay_payment_id = payment_id
    payment.save()

    cart = Cart.objects.filter(user=user)
    for c in cart:
        Order.objects.create(
                user=user,
                customer=customer,
                product=c.product,
                quantity=c.quantity,
                payment=payment
            )

        print("order is saved ")
        c.delete()
        print("cart is deleted")
    return redirect("orders")

@login_required
def orders(request):
    totalitem = 0
    wishitem = 0
    if request.user.is_authenticated:
        totalitem = len(Cart.objects.filter(user =request.user))
        wishitem = len(Wishlist.objects.filter(user = request.user))

    
    order_placed = Order.objects.filter(user=request.user)
    return render(request, "app/orders.html", locals())


from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Product, Cart 



 # Adjust import according to your models
@login_required
def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        
        c = Cart.objects.get(product=prod_id, user=request.user)
        c.quantity+=1
        c.save()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0 
        for p in cart:
            value = p.quantity*p.product.discounted_price
            amount  = value + amount
        totalamount = amount + 40
        data = {
            'quantity': c.quantity,
            'amount':amount,
            'totalamount':totalamount,
        }
        return JsonResponse(data)

@login_required
def minus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']

        c = Cart.objects.get(product=prod_id, user=request.user)
        c.quantity-=1
        c.save()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0 
        for p in cart:
            value = p.quantity*p.product.discounted_price
            amount  = value + amount
        totalamount = amount + 40
        print("total mamount calcltions done")
        data = {
            'quantity': c.quantity,
            'amount':amount,
            'totalamount':totalamount,
        }
        return JsonResponse(data)


from django.http import JsonResponse
from .models import Cart

@login_required
def remove_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']

        # Get the cart item
        c = Cart.objects.get(product_id=prod_id, user=request.user)

        # Reduce quantity
        if c.quantity > 1:
            c.quantity -= 1
            c.save()  # Save the updated quantity
        else:
            c.delete()  # Remove item from cart if quantity is 1

        # Recalculate amounts
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount += value
        totalamount = amount + 40  # Shipping cost

        # Return updated values as JSON
        data = {
            'quantity': c.quantity if c.quantity > 0 else 0,  # Ensure non-negative quantity
            'amount': amount,
            'totalamount': totalamount,
        }
        return JsonResponse(data)

"""@login_required
def remove_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']

        c = Cart.objects.get(product=prod_id, user=request.user)
        c.quantity-=1
        c.delete()
        user = request.user
        cart = Cart.objects.filter(user=user)
        amount = 0 
        for p in cart:
            value = p.quantity*p.product.discounted_price
            amount  = value + amount
        totalamount = amount + 40
        print("total mamount calcltions done")
        data = {
            'amount':amount,
            'totalamount':totalamount,
        }
        return JsonResponse(data)
    """


@login_required
def plus_wishlist(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        product = Product.objects.get(id=prod_id)
        user = request.user
        Wishlist(user=user, product=product).save()
        data={
            "message" : "Product is Added to Wishlist"
        }

        return JsonResponse(data)
    
@login_required
def minus_wishlist(request):
      if request.method == 'GET':
        prod_id = request.GET['prod_id']
        product = Product.objects.get(id=prod_id)

        user = request.user
        Wishlist.objects.filter(user=user, product=product).delete()

        data={
            "message" : "Product is Removed from Wishlist"
        }

        return JsonResponse(data)
    
