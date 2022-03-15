from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic import TemplateView, ListView
from cart.forms import CartAddProductForm
from .models import Category, Product
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from .forms import SignUpForm, RepairForm
from django.core.paginator import Paginator
from django.core.mail import send_mail
# Create your views here.

def homepage(request):
     return render(request, 'shop/product/home.html')

def repairspage(request):
     return render(request, 'shop/product/repairs.html')

def hoodpage(request):
    if request.GET.get('boob'): # write your form name here      
        bhoods = Product.objects.filter(category__slug='hoods')
        categories = Category.objects.all()
              
        try:
            status = Product.objects.filter(category__slug='hoods')
            categories = Category.objects.all()
            return render(request,"shop/product/black_hood.html",{'products':status, 'categories': categories, })
        except:
            return render(request,"shop/product/black_hood.html",{'products':status, 'categories': categories, })
    else:
        status = Product.objects.filter(category__slug='hoods')
        categories = Category.objects.all()
        return render(request, 'shop/product/black_hood.html', {'products':status, 'categories': categories, })

def btshirtpage(request):
    if request.GET.get('boob'): # write your form name here      
        btshirts = Product.objects.filter(category__slug='black-tshirts')
        categories = Category.objects.all()
              
        try:
            status = Product.objects.filter(category__slug='black-tshirts')
            categories = Category.objects.all()
            return render(request,"shop/product/black_shirt.html",{'products':status, 'categories': categories, })
        except:
            return render(request,"shop/product/black_shirt.html",{'products':status, 'categories': categories, })
    else:
        status = Product.objects.filter(category__slug='black-tshirts')
        categories = Category.objects.all()
        return render(request, 'shop/product/black_shirt.html', {'products':status, 'categories': categories, })

def ytshirtpage(request):
    if request.GET.get('boob'): # write your form name here      
        ytshirts = Product.objects.filter(category__slug='yellow-tshirts')
        categories = Category.objects.all()
              
        try:
            status = Product.objects.filter(category__slug='yellow-tshirts')
            categories = Category.objects.all()
            return render(request,"shop/product/yellow_shirt.html",{'products':status, 'categories': categories, })
        except:
            return render(request,"shop/product/yellow_shirt.html",{'products':status, 'categories': categories, })
    else:
        status = Product.objects.filter(category__slug='yellow-tshirts')
        categories = Category.objects.all()
        return render(request, 'shop/product/yellow_shirt.html', {'products':status, 'categories': categories, })

def product_list(request, category_slug=None):
    myproduct_list = Product.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(myproduct_list, 20) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    hoods = Product.objects.filter(category__name='hoods')
   
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
            'shop/product/list.html',
            {'category': category,
            'categories': categories,
            'products': products,
            'page_obj': page_obj,
            'hoods':hoods})

def product_detail(request, id, slug):
    product = get_object_or_404(Product,id=id,slug=slug,available=True)
    cart_product_form = CartAddProductForm()
    return render(request,
                  'shop/product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})

def signUpView(request):
    if request.method == "POST":
        form =SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request,user)
            return redirect('shop:product_list')

    else:
        form = SignUpForm()
    context = {
        'form':form,
    }
    return render(request,'shop/auth/signup.html',context)

def repair_form(request):
    if request.method == 'POST':
    # create object of form 
        form = RepairForm(request.POST) 
        if form.is_valid(): 
        # save the form data to model 
            form.save() 
    else:
        form = RepairForm()
    context = {
        'form':form,
    }
    return render(request,'shop/product/repair.html',  context)


def signInView(request):
    if request.method == 'POST':
        form =AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user =authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('shop:product_list')
            else:
                return redirect('shop:signup')
    else:
        form = AuthenticationForm()
    context = {
        'form':form,
    }
    return render(request,'shop/auth/signin.html',context)

def signoutView(request):
    logout(request)
    return redirect('shop:signin')



def search(request):
    if request.GET.get('boob'): # write your form name here      
        product_name =  request.GET.get('search')
        categories = Category.objects.all()
              
        try:
            status = Product.objects.filter(productname__icontains=product_name)
            categories = Category.objects.all()
            return render(request,"shop/product/search.html",{'products':status, 'categories': categories, })
        except:
            return render(request,"shop/product/search.html",{'products':status, 'categories': categories, })
    else:
        product_name =  request.GET.get('search')
        status = Product.objects.filter(name__icontains=product_name)
        categories = Category.objects.all()
        return render(request, 'shop/product/search.html', {'products':status, 'categories': categories, })

    
    
    
 


 
