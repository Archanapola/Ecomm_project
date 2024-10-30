from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
# Register your models here.
from .models import Cart, Order, Payment, Product, Customer, Wishlist

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'category', 'selling_price', 'discounted_price', 'available', 'product_img')
    """search_fields = ('title')
    list_filter = ('category', 'available')"""


@admin.register(Customer)

class CustomerModelAdmin(admin.ModelAdmin):

    list_display = ['id','name', 'mobile', 'city', 'state', 'zipcode']


@admin.register(Cart)

class CartModelAdmin(admin.ModelAdmin):

    list_display = ['id','user', 'products', 'quantity']

    def products(self, obj):
        link = reverse("admin:accounts_product_change", args=[obj.product.pk])
        return format_html('<a href="{}">{}</a>', link, obj.product.title)

@admin.register(Payment)

class CartModelAdmin(admin.ModelAdmin):

    list_display = ['id','user', 'amount', 'razorpay_order_id','razorpay_payment_status', 'razorpay_payment_id', 'paid']

@admin.register(Order)

class CartModelAdmin(admin.ModelAdmin):

    list_display = ['id','user','customers', 'products', 'quantity', 'status', 'payments', 'ordered_date', 'total_amount']

    def customers(self, obj):
        link = reverse("admin:accounts_customer_change", args=[obj.customer.pk])
        return format_html('<a href="{}">{}</a>', link, obj.product.title)

    def products(self, obj):
        link = reverse("admin:accounts_product_change", args=[obj.product.pk])
        return format_html('<a href="{}">{}</a>', link, obj.product.title)
    
    def payments(self, obj):
        link = reverse("admin:accounts_payment_change", args=[obj.payment.pk])
        return format_html('<a href="{}">{}</a>', link, obj.product.title)


@admin.register(Wishlist)

class CartModelAdmin(admin.ModelAdmin):

    list_display = ['id','user','products']
    def products(self, obj):
        link = reverse("admin:accounts_product_change", args=[obj.product.pk])
        return format_html('<a href="{}">{}</a>', link, obj.product.title)