from django.db import models
import datetime
from django.shortcuts import reverse

choice = (
    ('Top', 'Top'),
    ('Pants', 'Pants'),
    ('Skirts', 'Skirts'),
    ('Shorts', 'Shorts'),
)

colors = (
    ('Black', 'Black'),
    ('Navy', 'Navy'),
    ('Grey', 'Grey'),
)
# --------category-------- #

class Category(models.Model):
    name = models.CharField(max_length=50)

    @staticmethod
    def get_all_categories():
        return Category.objects.all()

    def __str__(self):
        return self.name
    
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField (max_length=50)
    phone = models.CharField(max_length=10)
    email=models.EmailField()
    password = models.CharField(max_length=100)

    #to save the data
    def register(self):
        self.save()


    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email= email)
        except:
            return False


    def isExists(self):
        if Customer.objects.filter(email = self.email):
            return True

        return False
    
class Order(models.Model):
    products = models.CharField(models.Products,on_delete=models.CASCADE)
    customer = models.CharField(Customer,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField (max_length=50, default='', blank=True)
    phone = models.CharField (max_length=50, default='', blank=True)
    date = models.DateField (default=datetime.datetime.today)
    status = models.BooleanField (default=False)

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')
    
class Products(models.Model):
    name = models.CharField(max_length=60)
    products_image = models.ImageField(null=True, blank=True)
    color = models.CharField(choices=colors, max_length=30)
    price= models.IntegerField(default=0)
    category= models.CharField(choices=choice, max_length=10)
    description= models.CharField(max_length=250, default='', blank=True, null= True)
    slug = models.SlugField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("myapp:products", kwargs={'slug': self.slug})
    
    

    @staticmethod
    def get_products_by_id(ids):
        return Products.objects.filter (id__in=ids)
    @staticmethod
    def get_all_products():
        return Products.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Products.objects.filter (category=category_id)
        else:
            return Products.get_all_products()
        
# class Bestseller(models.Model):
#     name = models.CharField(max_length=60)
#     products_image = models.ImageField(null=True, blank=True)
#     price= models.IntegerField(default=0)
#     category= models.CharField(choices=choice, max_length=10)
#     description= models.CharField(max_length=250, default='', blank=True, null= True)
#     slug = models.SlugField()

#     def __str__(self):
#         return self.name
    
#     def get_absolute_url(self):
#         return reverse("myapp:products", kwargs={'slug': self.slug})
    