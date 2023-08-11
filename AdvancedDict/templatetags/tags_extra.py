from django import template
register = template.Library()

@register.filter
def newitem(dictionary, key):
    return dictionary.get(key).lower()