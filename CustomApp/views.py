from django.template.response import TemplateResponse


def custom_app_view(request):
    context = {'title': 'Custom App', 'site_title': 'Custom App', 'site_header': 'Custom App',
               'index_title': 'Custom App', 'text': 'Custom App Text'}
    return TemplateResponse(request, 'admin/custom_app_view.html', context)
