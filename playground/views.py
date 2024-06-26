from django.shortcuts import render
from django.db.models import Q, F, Value, Func, ExpressionWrapper, DecimalField
from django.db.models.aggregates import Count, Max, Min, Avg, Sum
from django.db.models.functions import Concat
from django.db import transaction
from django.contrib.contenttypes.models import ContentType
from store.models import Product, OrderItem, Order, Customer
from tags.models import TaggedItem


def say_hello(request):
    
    return render(request, "hello.html", {"name": "Mosh", "result": ''})
