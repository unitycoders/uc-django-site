from django import template

register = template.Library()

@register.simple_tag
def fa_icon(name, title=None):
    tmp = ('title="%s"' % title) if title else ""
    return "<i class=\"fa fa-%s\" aria-hidden=\"true\" %s></i>" % (name,tmp)
