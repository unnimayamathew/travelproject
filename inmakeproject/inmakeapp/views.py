from urllib import request

from django.shortcuts import render

from inmakeapp.models import image


# Create your views here.
def demo(request):
    obj=image.objects.all()
    return render(request,"index.html",{'result':obj})
