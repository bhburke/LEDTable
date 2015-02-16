from django import template

register = template.Library()

@register.inclusion_tag('interface/int_option.html')
def int_option(name):
    return {'name' : name}

@register.inclusion_tag('interface/color_option.html')
def color_option():
    return {}

@register.inclusion_tag('interface/colors_option.html')
def color_list_option():
    return {}