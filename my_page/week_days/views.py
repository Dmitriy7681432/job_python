from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
# Create your views here.
week = {
    'sunday': "Воскресенье",
    'monday': "Понедельник",
    'tuesday': "Вторник",
    'wednesday': "Среда",
    'thursday': "Четверг",
    'friday': "Пятница",
    'saturday': "Суббота",
}


def get_week_days(request, days: str):
    description = week.get(days,None)
    if description:
        return HttpResponse(description)
    else:
        return HttpResponseNotFound(f'Неизвестный день недели {days}')

# def get_week_days(request, days: str):
#     return render(request, 'week_days/greeting.html')

def get_week_days_number(request, days: int):
    weeks = list(week)
    if 0<days<8:
        name_week = weeks[days-1]
        redirect_urls = reverse('week-name',args=(name_week, ))
        return HttpResponseRedirect(redirect_urls)
    else:
        if days>len(weeks):
            return HttpResponse(f'Неверный номер дня - {days}')