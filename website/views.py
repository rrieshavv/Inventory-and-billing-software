from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Laptop
# Create your views here.
def home(request):
    # user signed in
    if request.user.is_authenticated:
        return render(request,"index.html",{'page':'Home', 'home_status':'active'})
    
    #login post request
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "You are logged in. Welcome aboard!")
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials. Please try again!")
            return redirect('home')

    # user is not signed in
    return render(request, "login.html", {'page':'Log In'})

def logout_user(request):
    logout(request)
    messages.success(request, "You've been logged out!")
    return redirect('home')

def store(request):
    if request.user.is_authenticated:
        laptops = Laptop.objects.all()

        return render(request, "store.html", {'laptops':laptops, 'page':'Inventory', 'store_status':'active'})
    else:
        messages.error(request, "Please login to check the inventory.")
        return redirect('home')
    
def add_laptop(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            brand = request.POST['brand']
            model = request.POST['model']
            price = request.POST['price']
            qty = request.POST['qty']
            ram = request.POST['ram']
            chipset = request.POST['chipset']
            processor = request.POST['processor']
            storage = request.POST['storage']
            graphics = request.POST['graphics']
            operating_system = request.POST['operating_system']

            if not(brand and model and price and qty and ram and chipset and processor and storage and graphics and operating_system):
                messages.error(request, "Empty fields found!")
                pass
            
            try:
                qty = int(qty)
                price = float(price)

                if qty <= 0 :
                    messages.error(request, "Quanity cannot be 0 or lesser.")
                elif price <= 0:
                    messages.error(request, "Price cannot be 0 or lesser.")
                else:
                    new_laptop = Laptop(
                        brand=brand,
                        model=model,
                        price=price,
                        qty = qty,
                        ram = ram,
                        chipset = chipset,
                        storage = storage,
                        processor = processor,
                        graphics = graphics,
                        operating_sys = operating_system
                    )

                    new_laptop.save()
                    messages.success(request, "New laptop has been added to the stock! ")
                    return redirect('home')
            
            except ValueError:
                messages.error(request, "Incorrect Input found!")
                pass

            
        return render(request, "add_laptop.html", {'page':'Add laptop to stock','add_status':'active'})
    messages.error(request,"Please login to add a new laptop to the stock.")
    return redirect('home')

def store_item(request, pk):
    if request.user.is_authenticated:
        item = Laptop.objects.get(id=pk)
        return render(request, "laptop_detail.html", {"item":item, "page":"Store: "+item.model})
    else:
        messages.error(request,"Please login to view the laptop details.")
        return redirect('home')
