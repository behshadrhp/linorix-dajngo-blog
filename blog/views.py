from django.shortcuts import render
from .models import Essays

# Create your views here.


def index(request):
    # This function is for developing and making changes to the index file

    essay = Essays.objects.all()

    context = {'essay': essay}
    return render(request, 'src/index.html', context)


def view_essay(request , pk):
    # This function is for developing and making changes to the view essay file

    essay = Essays.objects.get(slug=pk)

    context = {'essay':essay}
    return render(request, 'src/view_essay.html' , context)