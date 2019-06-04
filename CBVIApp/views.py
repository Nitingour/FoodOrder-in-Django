from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from CBVIApp.models import Product,Cart
from django.core.mail import send_mail
from django.conf import settings
from django.db.models import Sum
# Create your views here.
class ProductList(ListView):
    model=Product
class ProductDetail(DetailView):
    model=Product
class ProductCreate(CreateView):
    model=Product
    fields='__all__'


def signupview(request):
    if request.method=='GET':
        sform=SignupForm()
        return render(request,"BlogApp/signup.html",{'sform':sform})
    if request.method=='POST':
        sform=SignupForm(request.POST)
        user=sform.save()
        user.set_password(user.password)
        user.save()
        sform=SignupForm()
        mydict={'sform':sform,'msg':'Registration Succssfully...'}
        return render(request,"BlogApp/signup.html",context=mydict)

def email(request):
    subject = 'Online Food Ordering'
    message = 'Welcome and Thank you for registration'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['ngour@edsystango.com',]
    send_mail( subject, message, email_from, recipient_list )
    return redirect('home')

def addcart(request):
    prodid=request.POST.get('pid')
    q=request.POST.get('quantity')
    price=request.POST.get('price')
    image=request.POST.get('image')
    total=float(q)*float(price)
    user=request.user
    Cart.objects.get_or_create(pid=prodid,quantity=q,user=user,price=price,image=image,total=total)
    product_list=Product.objects.all()
    count=Cart.objects.filter(user=user).count()
    mydict={'product_list':product_list,'msg':'Product added in Cart','count':count}
    return render(request,'CBVIApp/product_list.html',context=mydict)

def viewcart(request):
    user=request.user
    products=Product.objects.all()
    carts=Cart.objects.filter(user=user)
    gtotal=Cart.objects.filter(user=user).aggregate(int(sum('total')))
    mydict={'products':products,'carts':carts,'gtotal':gtotal}
    return render(request,'CBVIApp/cart_list.html',context=mydict)
