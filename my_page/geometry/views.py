from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
# Create your views here.
def get_rectangle_area(request,width:int,height:int):
    s = width*height
    # return HttpResponse(f"Площадь прямоугольника размером {width}x{height} равна {s}")
    return render(request, 'geometry/rectangle.html')
def get_square_area(request,width:int):
    s = width**2
    # return HttpResponse(f"Площадь квадрата размером {width}x{width} равна {s}")
    return render(request, 'geometry/square.html')

def get_circle_area(request,radius:int):
    s = 3.14*(radius**2)
    # return HttpResponse(f"Площадь круга радиусом {radius} равна {s}")
    return render(request, 'geometry/circle.html')

def func_rectangle(request,width:int,height:int):
    redirect_url = reverse('rectangle-name',args=(width,height))
    return HttpResponseRedirect(redirect_url)

def func_square(request,width:int):
    redirect_url = reverse('square-name', args=(width, ))
    return HttpResponseRedirect(redirect_url)

def func_circle(request,radius:int):
    redirect_url = reverse('circle-name', args=(radius, ))
    return HttpResponseRedirect(redirect_url)