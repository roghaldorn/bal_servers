from django import template
from django.db.models import F

register = template.Library()


@register.filter(name='frm_file_type')
def format_name(value):
    return f".{str(value).split('.')[-1]}"


@register.filter(name='frm_file_name')
def format_name(value):
    return str(value).split('/')[-1].split('.')[0]


@register.filter(name='frm_file_folder')
def format_name(value):
    return f"/{str(value).split('/')[0]}/"
