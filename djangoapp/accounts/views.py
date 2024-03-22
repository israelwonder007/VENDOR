from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
# Create your view here.
from .models import *
from .forms import OrderForm, CreateUserForm, CustomerForm
from .filters import OrderFilter

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
# from .decorations import unauthenticated_user, allowed_users, admin_only

# Create your views here.
# @unauthenticated_user
# def CustomerHomeView(request):
# @unauthenticated_user
def registerPage(request):
    # if request.user.is_authenticated:
    #     return redirect('home')
    # else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')

                messages.success(request, 'Account was created for'+' '+ username)
                return redirect('login')

        context = {'form':form}
        return render(request, 'accounts/register.html', context)
        
# @unauthenticated_user
def loginPage(request):
    user = User.objects.all() 
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # if user.is_staff:
            #     return redirect('dashboard')
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')
        
    context = {}
    return render(request, 'accounts/login.html', context)
    

def logoutUser(request):
    logout(request)
    return redirect('login')    

@login_required(login_url='login')
# @admin_only
def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    products = Product.objects.all()

    total_customers = customers.count()
    total_products = products.count()
    product_tag = Tag.objects.all().count()

    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {'orders':orders, 'customers':customers,'total_products':total_products,
               'product_tag':product_tag, 'total_orders':total_orders, 'total_customers':total_customers, 'delivered':delivered, 'pending':pending}

    return render(request, 'accounts/dashboard.html', context)

@login_required(login_url='login')
# @allowed_users(allowed_roles=['customer'])
def userPage(request):
    orders = request.user.customer.order_set.all()
    
    print('ORDER', orders)

    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    
    context = {'orders':orders, 'total_orders':total_orders, 'delivered':delivered, 'pending':pending}
    return render(request, 'accounts/user.html', context)

@login_required(login_url='login')
# @allowed_users(allowed_roles=['customer'])
def accountSettings(request):

    customer = request.user.customer
    form = CustomerForm(instance=customer)

    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()

    context = {'form':form}
    return render(request, 'accounts/account_settings.html', context)

@login_required(login_url='login')
# @allowed_users(allowed_roles=['customer'])
def createCustomer(request):

    # customer = request.user.customer
    form = CustomerForm()

    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()



    context = {'form':form}
    return render(request, 'accounts/create_customer.html', context)

# @login_required(login_url='login')
# @allowed_users(allowed_roles=['admin'])
def products(request):
    products = Product.objects.all()
    tagName = Tag.objects.all()
    

    product_count = products.count()

    context = {'products':products, 'tagName':tagName, 'product_count':product_count}
    return render(request, 'accounts/products.html', context)

def homeProducts(request):
    vendors = Product.objects.all()

    vendor_count = vendors.count()

    context = {'vendors':vendors, 'vendor_count': vendor_count}
    return render(request, 'accounts/home.html', context)

# @login_required(login_url='login')
# @allowed_users(allowed_roles=['admin'])
def customer(request, pk):
    customer = Customer.objects.get(id=pk)

    orders = customer.order_set.all()
    order_count = orders.count()

    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs
  
    context = {'customer':customer,  'orders': orders, 'order_count':order_count, 'myFilter':myFilter}
    return render(request, 'accounts/customer.html', context)

# @login_required(login_url='login')
# @allowed_users(allowed_roles=['admin'])
def createOrder(request, pk):
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'))
    customer = Customer.objects.get(id=pk)
    formset = OrderFormSet(instance= customer)

    
    if request.method == 'POST':
        # form = OrderForm(request.POST)
        formset = OrderForm(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')

    context = {'formset':formset}
    return render(request, 'accounts/order_form.html', context)

# @login_required(login_url='login')
# @allowed_users(allowed_roles=['admin'])
def updateOrder(request, pk):

    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        
    context = {'form':form}
    return render(request, 'accounts/order_form.html', context)

# @login_required(login_url='login')
# @allowed_users(allowed_roles=['admin'])
def deleteOrder(request, pk):

    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')
    
    context = {'item':order}
    return render(request, 'accounts/delete.html', context)