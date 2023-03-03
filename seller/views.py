
from itertools import product
from django.shortcuts import render, redirect
from random import randrange
from django.conf import settings
from .models import *
from buyer.models import *
from django.core.mail import send_mail




def seller_index(request):
    try:
       s_obj = Seller.object.get(email= request.request.session['seller_app_email'])
       return render(request, 'seller_index.html',{'seller_data':s_obj})
    except:
        return render(request,'seller_page_login.html' )

def seller_header(request):
    seller_obj = Seller.objects.get(email = request.session['seller_email'])
    return render(request, 'seller_header.html',{'seller_data':seller_obj})

def seller_add_product(request):
    return render(request, 'seller_add_product.html')

def my_product(request):
    return render(request, 'my_product.html')

def seller_app_profile(request):
    seller_obj = Seller.objects.get(email = request.session['seller_email'])
    if request.method == 'GET':
        return render(request, 'seller_app_profile.html',{'seller_data': seller_obj})
    else:
        seller_obj.full_name = request.POST['full_name']
        seller_obj.address = request.POST['address']
        seller_obj.gst_no = request.POST['gst_no']
        seller_obj.pic = request.FILES['pic']
        seller_obj.save() 
        return redirect('seller_ap_profile')


def seller_app_email(request):
    return render(request, 'seller_app_email.html')

def seller_page_register(request):
    if request.method == 'GET':
        return render(request,'seller_page_register.html')
    else:
        try:
            Buyer.objects.get(email = request.POST['email'])
            return render(request,'seller_page_register.html',{'msg':"Email is Already Exists!!!"})
        except:
            if request.POST['password'] == request.POST['repassword']:
                s = "Ecommerce Registration!!"
                global user_data
                user_data = [request.POST['first_name'], request.POST['last_name'], request.POST['email'], request.POST['password']]
                global c_otp
                c_otp = randrange(1000,9999) 
                m = f'Hello User!!\nYour OTP is {c_otp}'
                f = settings.EMAIL_HOST_USER
                r = [request.POST['email']]
                send_mail(s, m, f, r)  
                return render(request, 'otp.html', {'msg': 'Check Your MailBox'})
            else:
                return render(request, 'seller_page_register.html', {'msg': 'Both Passwords do not match!!'})

def seller_page_login(request):
    if request.method == 'POST':
        try:
            seller_obj = Seller.objects.get(email = request.POST['email'])
            if request.POST['password'] == seller_obj.password:
                request.session['seller_email'] = request.POST['email']
                return render(request, 'seller_index.html',{'seller_data': seller_obj})
            else:
                return render(request, 'seller_page_login.html', {'msg': 'Wrong Password!!'})

        except:
            return render(request, 'seller_page_login.html', {'msg': 'Email is Not Registered!!'})

    else:
        return render(request, 'seller_page_login.html')
    
def add_product(request):
    seller_obj = Seller.objects.get(email = request.session['seller_email'])
    if request.method == 'GET':
        return render(request, 'add_product.html', {'seller_data':seller_obj})
    else:
        Product.objects.create(
            product_name = request.POST['product_name'],
            des = request.POST['des'],
            price = request.POST['price'],
            product_stock = request.POST['product_stock'],
            pic = request.FILES['pic'],
            seller = seller_obj
        )
        return redirect('add_product')


def seller_logout(request):
    del request.session['seller_email']
    return redirect('seller_page_login')    
