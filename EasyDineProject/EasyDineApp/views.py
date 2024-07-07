from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from rest_owner.models import Restaurant
# from .forms import BookingForm
from EasyDineApp.models import Booking

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages


# Create your views here.
def index(request):
    #messages.success(request, "this is a test message")
    return render(request, 'EasyDineApp/index.html')
    #return HttpResponse("this is homepage")

def about(request):
    return render(request, 'EasyDineApp/about.html')
   
def contact(request):
    return render(request, 'EasyDineApp/contact.html')

def booking(request):
    return render(request, 'EasyDineApp/booking.html')

def service(request):
    return render(request, 'EasyDineApp/service.html')

def rest_list(request):
    return render(request, 'EasyDineApp/restList.html')

def restDetails(request):
    return render(request, 'EasyDineApp/restDetails.html')

#add login module
#def login(request):
#    return render(request, 'EasyDineApp/login.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful')
            return redirect('home')  # replace 'home' with your desired URL name
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'EasyDineApp/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')  # replace 'login' with your login URL name

def paymentSuccess(request):
    latest_booking = Booking.objects.latest('id')
    total_payment = 50*latest_booking.people
    return render(request, 'EasyDineApp/paymentSuccess.html', {'latest_booking':latest_booking, 'total_payment':total_payment})

def payment(request):
    latest_booking = Booking.objects.latest('id')
    total_payment = 50*latest_booking.people
    return render(request, 'EasyDineApp/payment.html', {'latest_booking':latest_booking, 'total_payment':total_payment})

def paymentInvoice(request):
    return render(request, 'EasyDineApp/paymentInvoice.html')

def restaurantDetails(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    return render(request, 'EasyDineApp/restDetails.html', {'restaurant':restaurant})

def rest_list(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'EasyDineApp/restList.html', {'restaurants':restaurants})
        
        
def booktable(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        datetime = request.POST['datetime']
        people = request.POST['people']
        phone = request.POST['phone']
        booking=Booking.objects.create(name=name, email=email, datetime=datetime, people=people, phone=phone)
        booking.save()
        messages.success(request, 'Wooh!Your Table is scheduled') 
        #payment_summary
        latest_booking = Booking.objects.latest('id')
        total_payment = 50*latest_booking.people
        return render(request, 'EasyDineApp/paymentInvoice.html', {'latest_booking':latest_booking, 'total_payment':total_payment})
    return render(request, 'EasyDineApp/booking.html')



































           
    
