from django import template

register = template.Library()

@register.filter
def dictkey(form, key):
    try:
        return form[key]
    except KeyError:
        return ''