from django.shortcuts import render
from .models import Proizvod
# Create your views here.
def home_page(request):
    proizvods = Proizvod.objects.all()
    context = {
        'proizvods': proizvods
    }
    return render(request, "index.html", context)
