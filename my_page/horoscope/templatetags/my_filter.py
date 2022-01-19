from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()
@register.filter(name='split')
#Гарантирует чтобы в аргумент value приходило строковое значение
@stringfilter
def split(value, key=' '):
    return value.split(key)
# register.filter('split', split)
