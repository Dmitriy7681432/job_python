from django.urls import path
from . import views

urlpatterns = [
    path('rectangle/<int:width>/<int:height>',views.get_rectangle_area,name="rectangle-name"),
    path('square/<int:width>',views.get_square_area,name="square-name"),
    path('circle/<int:radius>',views.get_circle_area,name="circle-name"),
    path('get_rectangle_area/<int:width>/<int:height>', views.func_rectangle),
    path('get_square_area/<int:width>', views.func_square),
    path('get_circle_are/<int:radius>', views.func_circle),

]