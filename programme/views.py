from django.shortcuts import render

from .models import Programme


def index(request, template='programme.html'):
    programme = Programme.objects.filter(is_active=True).first()

    if programme:
        return render(request, template, {'programme': programme})

    return render(request, 'not_found.html')
