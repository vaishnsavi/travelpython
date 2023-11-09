from django .http  import HttpResponse
from django.shortcuts import render
from .models import place, item

def demo(request):
    places = place.objects.all()
    items = item.objects.all()
    return render(request, "index.html", {'places': places, 'items': items})
