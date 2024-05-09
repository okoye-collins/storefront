from django.shortcuts import render
from django.db.models import Q, F, Value, Func, ExpressionWrapper, DecimalField
from django.db.models.aggregates import Count, Max, Min, Avg, Sum
from django.db.models.functions import Concat
from store.models import Product, OrderItem, Order, Customer


def say_hello(request):
    
    product = Product.objects.annotate(
        top_selling= Sum(F('orderitem__unit_price')*F('orderitem__quantity'))
    )

    
    return render(request, 'hello.html', {'name':'Mosh', 'result': product})