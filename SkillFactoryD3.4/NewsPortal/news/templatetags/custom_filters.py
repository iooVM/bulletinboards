from django import template

register = template.Library()  # если мы не зарегистрируем наши фильтры, то Django никогда не узнает, где именно их искать и фильтры потеряются

@register.filter(name='censor')
def censor(value):
    censorword = ['A']
    for word in censorword:
        value = value.replace(word, '*****')
    return value


