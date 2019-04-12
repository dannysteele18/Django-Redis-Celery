from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader

from .models import Item

def index(request):
    items = Item.objects.order_by('birthday')

    template = loader.get_template('xmlfeed/index.html')
    context = {
        'items': items,
    }

    return HttpResponse(template.render(context, request))