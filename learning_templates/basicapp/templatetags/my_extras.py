from django import template
register = template.Library()

@register.filter(name='cutout')
def cutout(value,arg):
   """This  cuts out all values of "arg"  from the string"""
   return value.replace(arg,'')

