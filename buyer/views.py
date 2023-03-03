from django.shortcuts import redirect,render
from .models import Buyer
from django.core.mail import send_mail
from random import randrange
from django.conf import settings
# Create your views here.

def index(request):
    try:
        buyer_row = Buyer.objects.get(email = request.session['email'])
        return render(request,'index.html',{'user_data': buyer_row})
    except:
        return render(request,'index.html')

def about(request):
    buyer_row = Buyer.objects.get(email = request.session['email'])
    return render(request,'about.html',{'user_data': buyer_row})

def contact(request):
    buyer_row = Buyer.objects.get(email = request.session['email'])
    return render(request,'contact.html',{'user_data' : buyer_row})

def cycle(request):
    buyer_row = Buyer.objects.get(email = request.session['email'])
    return render(request,'cycle.html',{'user_data' : buyer_row})

def news(request):
    buyer_row = Buyer.objects.get(email = request.session['email'])
    return render(request,'news.html',{'user_data' : buyer_row})

def add_row(requset):
    Buyer.objects.create(
        first_name = 'meet',
        last_name = 'gdiya',
        password = 'meet@2001',
        email = 'meet@email.com',
        address = '315,316 hari,surat',
        mobile = '4527864589',
    )
    return render(requset,'success.html')

def register(request):
    if request.method == 'GET':
        return render(request,'register.html')
    else:
        pass

        try:
            Buyer.objects.get(email = request.POST['email'])
            return render(request,'register.html',{'msg':"Email is Already Exists!!!"})
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
                return render(request, 'register.html', {'msg': 'Both Passwords do not match!!'})
            
def otp(request):
    if str(c_otp) == request.POST['otp']:
        Buyer.objects.create(
            first_name = user_data[0],
            last_name = user_data[1],
            email = user_data[2],
            password = user_data[3]
        )
        return render(request, 'register.html', {'msg': 'Account created successfully!!'})
    else:
        return render(request, 'otp.html', {'msg': 'Wrong OTP enter again!!'})  

def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        try:
            buyer_row = Buyer.objects.get(email = request.POST['email'])
            if request.POST['password'] == buyer_row.password:
                request.session['email'] = request.POST['email']
                return render(request, 'index.html',{'user_data':buyer_row})
            else:
                return render(request,'login.html',{'msg':'wrong password!!'})
        except:
            return render(request,'login.html',{'msg':'email is not registered!!'})
        
def logout(request):
    del request.session['email']
    return redirect('index')