from django.urls import path, register_converter
from . import views,converters
register_converter(converters.FourDigitYearConverter, 'yyyy')
register_converter(converters.MyFloatConverter, 'my_float')
register_converter(converters.MyDateConverter, 'my_date')

urlpatterns = [
    path('', views.index, name='horoscope-index'),
    path('type', views.type),
    path('<my_date:sign_zodiak>', views.get_my_date_converters),
    path('<yyyy:sign_zodiak>', views.get_yyyy_converters),
    path('<int:sign_zodiak>', views.get_info_about_sign_zodiak_by_number),
    path('<my_float:sign_zodiak>', views.get_my_float_converters),
    path('<int:month>/<int:day>', views.get_info_about_date),
    path('type/<type_zodiaks>', views.get_info_about_type_zodiak, name='horoscope-type'),
    # path('type', views.sign_type_list),
    # path('type/<sign_type>', views.sign_type_page, name='sign_type_page'),
    path('<str:sign_zodiak>', views.get_info_about_sign_zodiak, name='horoscope-name'),

]