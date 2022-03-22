from django.contrib import admin

# Register your models here.
from .models import Category, Product, Repair

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug']
	prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug', 'price','available', 'created', 'updated']
	list_filter = ['available', 'created', 'updated']
	list_editable = ['price', 'available']
	prepopulated_fields = {'slug': ('name',)}

@admin.register(Repair)
class RepairAdmin(admin.ModelAdmin):
	list_display = ['name', 'phone_number','email','description','created','device_type','SHALL_WE_PICK_OR_YOULL_BRING_THE_DEVICE']
	