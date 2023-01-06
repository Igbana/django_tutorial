from django.shortcuts import render, redirect
from .forms import OrderForm
from django.forms import formset_factory
from .models import *

# Create your views here.
def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    total_orders = orders.count()
    orders_delivered = orders.filter(status='Delivered').count()
    orders_pending = orders.filter(status='Pending').count()
    context = {
        'orders': orders,
        'customers': customers,
        'total_orders': total_orders,
        'orders_delivered': orders_delivered,
        'orders_pending': orders_pending,
    }
    return render(request, 'screens/dashboard.html', context=context)

def product(request):
    products = Product.objects.all()

    return render(request, 'screens/products.html', context={'products': products})

def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    order = customer.order_set.all()
    total_orders = order.count()
    context = {
        'orders': order,
        'customer': customer,
        'total_orders': total_orders,
    }
    print(order)
    return render(request, 'screens/customers.html', context=context)

def create_order(request, pk):
    customer = Customer.objects.get(id=pk)
    # OrderFormSet = formset_factory(Customer, Order, fields=('product', 'status'))
    form = OrderForm(initial={'customer': customer})
    # formset = OrderFormSet(instance=customer)
    context = {'form': form}
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    return render(request, 'screens/order.html', context=context)

def update_order(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}

    return render(request, 'screens/order.html', context=context)

def delete_order(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')
    context = {
        'item': order
    }
    return render(request, 'screens/delete.html', context=context)