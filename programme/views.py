from django.shortcuts import render
from django.utils import timezone

from .models import Programme


def index(request, date=None):
    today = timezone.now().date()

    if date is not None:
        programme = Programme.objects.filter(date=date).first()
    else:
        # Récupérer le programme futur le plus proche
        programme = Programme.objects.filter(is_active=True, date__gte=today).order_by('date').first()

    # Si aucun programme futur n'existe, récupérer le dernier programme passé
    if not programme:
        programme = Programme.objects.filter(is_active=True, date__lte=today).order_by('-date').first()

    if programme:
        programme.nb_views += 1
        programme.save()
        context = {
            'pagetitle': f"Programme du {programme.date.strftime('%d %B %Y')}",
            'programme': programme
        }
        return render(request, 'programme.html', context)

    return render(request, 'not_found.html')
