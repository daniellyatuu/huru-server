from django import template
import pytz
import datetime

register = template.Library()


@register.filter(name="dateformat")
def dateformat(value):
    if value:
        value = value.astimezone(pytz.timezone('Africa/Dar_es_Salaam'))
        value = datetime.datetime.strftime(value, '%b %d, %Y %H:%M')
    else:
        pass  # value
    return value
