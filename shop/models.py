from django.db import models
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

SHALL_WE_PICK_OR_YOULL_BRING_THE_DEVICE = (
	('please pick up the device','Please pick up the device'),
	('i shall come to the shop','I shall come to the shop')
	)

class Category(models.Model):
	name = models.CharField(max_length=200,db_index=True)
	slug = models.SlugField(max_length=200,unique=True)
	class Meta:
		ordering = ('name',)
		verbose_name = 'category'
		verbose_name_plural = 'categories'
	def __str__(self):
		return self.name
	def get_absolute_url(self):
		return reverse('shop:product_list_by_category',args=[self.slug])

class Product(models.Model):
	category = models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE)
	name = models.CharField(max_length=200, db_index=True)
	slug = models.SlugField(max_length=200, db_index=True)
	image = models.ImageField(upload_to='products/%Y/%m/%d',blank=True)
	description = models.TextField(blank=True)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	available = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	class Meta:
		ordering = ('name',)
		index_together = (('id', 'slug'),)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('shop:product_detail',
					args=[self.id, self.slug])

class Repair(models.Model):
    DEVICE_TYPES =[
('phone ','Phone'),
('tv', 'Tv'),
('laptop','Laptop')
]
	

    name= models.CharField(max_length=100)
    email= models.EmailField()
    phone_number = PhoneNumberField(blank=True)
    description = models.TextField(blank=True) 
    created = models.DateTimeField(auto_now_add=True,blank=True)
    device_type= models.CharField(max_length=100,choices=DEVICE_TYPES)
    SHALL_WE_PICK_OR_YOULL_BRING_THE_DEVICE= models.CharField(max_length=100,choices=SHALL_WE_PICK_OR_YOULL_BRING_THE_DEVICE, default='i shall come to the shop')
    def __str__(self): 
        return self.name
