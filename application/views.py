from django.shortcuts import render


def index(request):
    context = dict()
    context['hello'] = 'Hello World!'
    return render(request, template_name="application/index.html", context=context)
