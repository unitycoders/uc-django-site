from django import template

register = template.Library()

@register.simple_tag
def fa_icon(name):
    return "<i class=\"fa fa-%s\" aria-hidden=\"true\"></i>" % (name,)
