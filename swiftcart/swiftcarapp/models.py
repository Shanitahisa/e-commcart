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

class Favorite(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="favorites")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="favorited_by")
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "product")  # prevent duplicate favorites

    def __str__(self):
        return f"{self.user.username} → {self.product.pName}"
