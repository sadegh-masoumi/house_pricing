from django import template
import hashlib

register = template.Library()


@register.filter()
def md5_string(value):
    return hashlib.md5(value.encode()).hexdigest()
