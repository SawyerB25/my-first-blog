from django import template
from django import template
from django.utils.html import escape
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(is_safe=True)
def smart_truncate(texte, nb_caracteres):
    try:
        nb_caracteres = int(nb_caracteres)
    except ValueError:
        return texte

    if len(texte) <= nb_caracteres:
        return texte

    texte = texte[:nb_caracteres + 1]

    if texte[-1:] != ' ':
        mots = texte.split(' ')[:-1]
        texte = ' '.join(mots)
    else:
        texte = texte[0:-1]
