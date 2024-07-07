from django.shortcuts import render, HttpResponse, redirect
from EasyDineApp.models import Booking
from django.core.paginator import Paginator


# Create your views here.

def index(request):
    return render(request, 'rest_owner/index.html')

def payment(request):
    return render(request, 'rest_owner/payment.html')

def dashboard(request):
    return render(request, 'rest_owner/dashboard.html')

def login(request):
    return render(request, 'rest_owner/login.html')

def feedback(request):
    return render(request, 'rest_owner/feedback.html')

def addrestaurant(request):
    return render(request, 'rest_owner/addrestaurant.html')

def editrestaurant(request):
    return render(request, 'rest_owner/editrestaurant.html')

def signup(request):
    return render(request, 'rest_owner/signup.html')

def dashboard(request):
    bookings =Booking.objects.order_by('-id') 
    return render(request, 'rest_owner/dashboard.html', {'bookings':bookings})
    

#add restaurant form subbmission on databse
from .models import Restaurant
# from .forms import RestaurantForm

def addrestaurant(request):
    if request.method == 'POST':
        name = request.POST['name']
        address = request.POST['address']
        post = request.POST['post']
        city = request.POST['city']
        about = request.POST['about']
        phone = request.POST['phone']
        image = request.FILES['upload']
        
        restaurant = Restaurant(
            name=name,
            address=address,
            post=post,
            city=city,
            about=about,
            phone=phone,
            image=image
        )
        
        restaurant.save()
        return redirect('dashboard.html')  # Redirect to a page where you display all restaurants
    
    return render(request, 'rest_owner/addrestaurant.html')