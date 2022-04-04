from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
path('shop/', views.product_list, name='product_list'),
path('black-hoods/', views.hoodpage, name='bhoods'),
path('black-tshirts/', views.btshirtpage, name='btshirts'),
path('yellow-tshirts/', views.ytshirtpage, name='ytshirts'),
path('repairs/', views.repair_form, name='repairs'),
path('', views.homepage, name='home'),
path('categories/<slug:category_slug>/', views.product_list,
	name='product_list_by_category'),
path('<int:id>/<slug:slug>/', views.product_detail,
	name='product_detail'),
path('account/created/',views.signUpView,name = 'signup'),
path('account/signin/',views.signInView,name = 'signin'),
path('account/logout/',views.signoutView,name = 'signout'),
path('search/', views.search, name='search'),
path('dan/', views.index, name='index'),
path('dan/daraja/stk-push', views.stk_push_callback, name='mpesa_stk_push_callback'),

]
