from django.views.generic import TemplateView


class MainIndexView(TemplateView):
    template_name = 'front/index.html'
    extra_context = {
        'title': 'Bal Servers'
    }
