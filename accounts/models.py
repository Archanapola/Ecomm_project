from django.db import models
from django.contrib.auth.models  import User
# Create your models here.
from django.db import models

CATEGORY_CHOICES = (
    ('saree', 'Saree'),
    ('partywear', 'Party Wear'),
    ('ethnicwear', 'Ethnic Wear'),
    ('casualwear', 'Casual Wear'),
    ('weddingwear', 'Wedding Wear'),
    ('kurta', 'Kurta'),
    ('lehenga', 'Lehenga'),
    ('tops', 'Tops'),
)


class Product(models.Model):
    # Basic product info
    title = models.CharField(max_length=255)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)  # e.g., 2999.99
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    description = models.TextField()
    material = models.CharField(max_length=100)
    
    # Category and product type
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=20)
    
    # Stock and availability
    stock = models.IntegerField(default=0)
    available = models.BooleanField(default=True)
    
    # Product images
    product_img = models.ImageField(upload_to='product')
    
    # Optional additional product fields
    additional_info = models.TextField(blank=True, null=True)  # Can be used for sizing info, care instructions, etc.
    color = models.CharField(max_length=50, blank=True, null=True)  # Color options
    size = models.CharField(max_length=20, blank=True, null=True)  # e.g., S, M, L, XL, etc.



    def __str__(self):
        return self.title
    
STATE_CHOICES = (
   ("AN","Andaman and Nicobar Islands"),
   ("AP","Andhra Pradesh"),
   ("AR","Arunachal Pradesh"),
   ("AS","Assam"),
   ("BR","Bihar"),
   ("CG","Chhattisgarh"),
   ("CH","Chandigarh"),
   ("DN","Dadra and Nagar Haveli"),
   ("DD","Daman and Diu"),
   ("DL","Delhi"),
   ("GA","Goa"),
   ("GJ","Gujarat"),
   ("HR","Haryana"),
   ("HP","Himachal Pradesh"),
   ("JK","Jammu and Kashmir"),
   ("JH","Jharkhand"),
   ("KA","Karnataka"),
   ("KL","Kerala"),
   ("LA","Ladakh"),
   ("LD","Lakshadweep"),
   ("MP","Madhya Pradesh"),
   ("MH","Maharashtra"),
   ("MN","Manipur"),
   ("ML","Meghalaya"),
   ("MZ","Mizoram"),
   ("NL","Nagaland"),
   ("OD","Odisha"),
   ("PB","Punjab"),
   ("PY","Pondicherry"),
   ("RJ","Rajasthan"),
   ("SK","Sikkim"),
   ("TN","Tamil Nadu"),
   ("TS","Telangana"),
   ("TR","Tripura"),
   ("UP","Uttar Pradesh"),
   ("UK","Uttarakhand"),
   ("WB","West Bengal")
)
    
class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    mobile = models.IntegerField(default=0)
    city = models.CharField(max_length=100)
    state = models.CharField(choices=STATE_CHOICES, max_length=100)
    zipcode = models.IntegerField()

    def __str__(self):
        return self.name
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_cost(self):
        return self.quantity*self.product.discounted_price


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField()
    razorpay_order_id = models.CharField(max_length=100, blank=True, null=True)
    razorpay_payment_status = models.CharField(max_length=100, blank=True, null=True)
    razorpay_payment_id = models.CharField(max_length=100, blank=True, null=True)
    paid = models.BooleanField(default=False)

class Order(models.Model):
    ORDER_STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Shipped', 'Shipped'),
        ('Out for Delivery', 'Out for Delivery'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
    ]

  

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True, related_name='customer_orders')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default='Pending')
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, default="")
    ordered_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return f"Order {self.id} - {self.user.username} - {self.status}"
    
    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price



class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)