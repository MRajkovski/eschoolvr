from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
import json

from .models import *
from .forms import *


# Create your views here.



def registerPage(request):
    if request.user.is_authenticated:
        return redirect('courses')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')

                Student.objects.create(user=user,)
                
                messages.success(request,'Account was created for '+username)

                return redirect('login')

        context = {'form':form}
        return render(request, 'vrschool/register.html',context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('courses')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request,user)
                return redirect('courses')
            else:
                messages.info(request,'Username or Password is incorrect')

        context={}
        return render(request, 'vrschool/login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def editProfile(request):
    context={}
    return render(request,'vrschool/editprofile.html',context)

@login_required(login_url='login')
def courses(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartItems = order['get_cart_items']
        
    courses = Course.objects.all()
    context = {'courses':courses, 'cartItems':cartItems}
    return render(request,'vrschool/courses.html',context)
    
@login_required(login_url='login')
def userPage(request):
    
    courses = request.user.order_set.all()
    print('COURSES',courses)
    context = {'courses':courses}
    return render(request, 'vrschool/user.html',context)

@login_required(login_url='login')
def helpPage(request):

    context = {}
    return render(request,'vrschool/help.html',context)

@login_required(login_url='login')
def starterPage(request):

    context = {}
    return render(request,'vrschool/starter.html',context)


@login_required(login_url='login')
def chatPage(request):

    context = {}
    return render(request,'vrschool/chat.html',context)

@login_required(login_url='login')
def cart(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartItems = order['get_cart_items']


    context = {'items':items, 'order':order,'cartItems':cartItems}
    return render(request,'vrschool/cart.html',context)

@login_required(login_url='login')
def checkout(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartItems = order['get_cart_items']

    context = {'items':items, 'order':order,'cartItems':cartItems}
    return render(request,'vrschool/checkout.html',context)

@login_required(login_url='login')
def updateItem(request):
    data = json.loads(request.body)
    courseId = data['courseId']
    action = data['action']

    print('Action:', action)
    print('courseId:', courseId)

    customer = request.user
    course = Course.objects.get(id=courseId)

    order,created = Order.objects.get_or_create(customer=customer,complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order,course=course)

    orderItem.save()

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added',safe=False)