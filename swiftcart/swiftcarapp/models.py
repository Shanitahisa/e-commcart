from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


# Create your models here.
class CustomUser(AbstractUser):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ]
    phone_contact = models.CharField(max_length=15,blank=True, null = True)  
    address = models.CharField(max_length=30,blank=True, null = True) 
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, blank= True, null = True)
    email = models.EmailField(max_length=50,blank=True,null=True)
   
    def __str__(self):
        return self.username 
    
class Product(models.Model):
    CAT_CHOICES=[
        ("apparel","Apparel"),
        ("accesories","Accessories"),
        ("shoes","Shoes"),
        ("suits","Suites"),
        ("gaming&spots","Gaming&sports"),

    ]

    GEN_CCHOICES=[
        ("ladies","Ladies"),
        ("gents", "Gents"),
        ("unisex","Unisex"),
        ("kids","Kids"),

    ]
    pName=models.CharField(max_length=20,blank=True,null=True)
    pPrice = models.IntegerField(blank=True,null=True)
    pDescription = models.CharField(max_length=100, blank=True, null=True)
    pCategory = models.CharField(
        max_length=20,
        choices=CAT_CHOICES,
        default="apparel",
    )
    pGender=models.CharField(
        max_length=20,
        choices=GEN_CCHOICES,
        default="unisex",
    )
    pImage=models.ImageField(upload_to='pimages/',blank=True)
    pPostdate=models.DateField(auto_now=True)

    def __str__(self):
        return self.pName 

# class Cart(models.Model):
#     customUser = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
#     date_created = models.DateTimeField(auto_now_add=True)

#     def update_total_price(self):
#         cart_items = self.cartitem_set.all()
#         total = sum(item.subtotal for item in cart_items)
#         self.total_price = total
#         self.save()
#     # other fields like total price, date_created, etc.

# class CartItem(models.Model):
#     cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField()
#     @property
#     def price(self):
#         return self.product.pPrice

#     # subtotal can be calculated based on quantity and price
#     @property
#     def subtotal(self):
#         return self.quantity * self.product.pPrice
#     # other fields like price, subtotal, etc

#     def save(self, *args, **kwargs):
#         super().save(*args, **kwargs)
#         self.cart.update_total_price()


# class checkout(models.Model):
#     CustomUser = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     order_date = models.DateTimeField(auto_now_add=True)

#     # Add other fields as needed

#     def __str__(self):
#         return f"Order #{self.pk} - {self.product.pName}"