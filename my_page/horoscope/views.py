from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
znak_zodiak = {
    'aries': 'Овен - первый знак зодиака (c 21 марта по 20 апреля)',
    'taurus': 'Телец - второй знак зодиака (c 21 апреля по 21 мая)',
    'gemini': 'Близнецы - третий знак зодиака (c 22 мая по 21 июня)',
    'cancer': 'Рак - четвертый знак зодиака (c 22 июня по 20 июля)',
    'leo': "Лев - <i>пятый знак зодиака</i> (c 23 июля по 21 августа)",
    'virgo': "Дева - шестой знак зодиака (c 22 августа по 23 сентября)",
    'libra': "Весы - седьмой знак зодиака (c 24 сентября по 23 октября)",
    'scorpion': "Скорпион - воьсмой знак зодиака (c 24 октября по 22 ноября)",
    'sagittarius': "Стрелец - девятый знак зодиака (c 23 ноября по 22 декабря)",
    'capricorn': "Козерог - десятый знак зодиака (c 23 декабря по 20 января)",
    'aquarius': "Водолей - одиннадцатый знак зодиака (c 21 января по 19 февраля)",
    'pisces': "Рыбы - двенадцатый знак зодиака (c 20 февраля по 20 марта)",
}

type_zodiak = {
    'fire': ['aries', 'leo', 'sagittarius'],
    'air': ['gemini', 'libra', 'aquarius'],
    'water': ['canser', 'leo', 'pisces'],
    'land': ['taurus', 'virgo', 'caprirorn'],
}


# sign_types_dict = {
#     'fire': ['aries', 'leo', 'sagittarius'],
#     'air': ['gemini', 'libra', 'aquarius'],
#     'water': ['canser', 'leo', 'pisces'],
#     'land': ['taurus', 'virgo', 'caprirorn'],
# }

def get_my_date_converters(request, sign_zodiak):
    return HttpResponse(f'Вы передали дату - {sign_zodiak}')


def get_yyyy_converters(request, sign_zodiak):
    return HttpResponse(f'Вы передали число из 4х цифр - {sign_zodiak}')


def get_my_float_converters(request, sign_zodiak):
    return HttpResponse(f'Вы передали вещественное число - {sign_zodiak}')


def index(request):
    zodiaks = list(znak_zodiak)
    # li_elements += f"<li> <a href='{redirect_path}'>{sign.title()} </a> </li>"
    context = {
        'zodiaks': zodiaks,
        "znak_zodiak": {}
    }
    return render(request,'horoscope/index.html',context=context)


# def get_info_about_sign_zodiak(request, sign_zodiak: str):
#     description = znak_zodiak.get(sign_zodiak, None)
#     if description:
#         return HttpResponse(f'<h2>{description}</h2>')
#     else:
#         return HttpResponseNotFound(f'Неизвестный знак зодиака - {sign_zodiak}')

def get_info_about_sign_zodiak(request, sign_zodiak: str):
    description = znak_zodiak.get(sign_zodiak)
    data = {
        'description': description,
        'sign': sign_zodiak,
        'zodiaks': znak_zodiak,

    }
    return render(request, 'horoscope/info_zodiak.html', context=data)


def get_info_about_sign_zodiak_by_number(request, sign_zodiak: int):
    zodiaks = list(znak_zodiak)
    if sign_zodiak > len(zodiaks):
        return HttpResponse(f"Неправильный порядковый номер знака зодиака - {sign_zodiak}")
    name_zodiak = zodiaks[sign_zodiak - 1]
    redirect_url = reverse('horoscope-name', args=(name_zodiak,))
    return HttpResponseRedirect(redirect_url)


def get_info_about_type_zodiak(request, type_zodiaks: str):
    description = type_zodiak.get(type_zodiaks, None)
    print('+++++++++++++++', type_zodiaks)
    li_elements = "Нет такой стихии"
    if type_zodiaks in type_zodiak:
        li_elements = ''
        for i in description:
            print('********', i)
            redirect_path = reverse('horoscope-name', args=[i])
            li_elements += f"<li><a href='{redirect_path}'>{i.title()}</a></li>"
            print('li_elements', li_elements)
    return HttpResponse(f'<ul>{li_elements}</ul>')


def type(request):
    type_znak_zodiaks = list(type_zodiak)
    li_elements = ''
    for sign in type_znak_zodiaks:
        print('---------', sign)
        redirect_path = reverse('horoscope-type', args=[sign])
        li_elements += f"<a href='{redirect_path}'><li>{sign.title()}</li></a>"
        print(li_elements)
    return HttpResponse(f'<ul>{li_elements}</ul>')


def get_info_about_date(request, month, day):
    li_elements = ''
    if (month == 3 and 20 < day < 32) or (month == 4 and 19 < day < 31):
        # type_z = znak_zodiak.get('aries')
        result = 'aries'
        # for i in type_z:
        # if i == 'aries':
        url = reverse('horoscope-name', args=[result])
        # li_elements += f"<li><a href='{redirect_path}'>{i.title()}</a></li>"
        li_elements += f"<a href='{url}'><li>{result.title()}</li></a>"
        print('li_elements', li_elements)
        return HttpResponse(f'<h2>{li_elements}</h2>')

# def sign_type_list(request):
#     result = ''
#     for element in list(sign_types_dict):
#         url = reverse('sign_type_page', args=[element])
#         result += f'<a href="{url}"><li>{element.title()}</li></a>'
#     return HttpResponse(f'<ul>{result}</ul>')
#
# def sign_type_page(request, sign_type):
#     result = "Нет такой стихии."
#     if sign_type in sign_types_dict:
#         result = ''
#         for st in sign_types_dict[sign_type]:
#             sign_url = reverse('horoscope-name', args=[st])
#             result += f'<a href="{sign_url}"><li>{st.title()}</a></li>'
#     return HttpResponse(f'<ul>{result}</ul>')
