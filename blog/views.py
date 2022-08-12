from django.shortcuts import render
from .models import Essays

# Create your views here.


def index(request):

    essay = Essays.objects.all()

    context = {'essay': essay}
    return render(request, 'src/index.html', context)