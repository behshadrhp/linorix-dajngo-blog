from django.shortcuts import render , redirect
from .models import Essays
from .forms import EssayForm

# Create your views here.


def index(request):
    # This function is for developing and making changes to the index file

    essay = Essays.objects.all()

    context = {'essay': essay}
    return render(request, 'src/index.html', context)


def essay(request):
    # this function is for creating and changing and developing essay .

    form = EssayForm
    
    if request.method == 'POST':
        form = form(request.POST)
        if form.is_valid():
            # create new Essay
            form.save()
            return redirect('index')


    context = {'form':form}
    return render(request, 'src/essay_form.html' , context)
    

def view_essay(request , pk):
    # This function is for developing and making changes to the view essay file

    essay = Essays.objects.get(slug=pk)

    context = {'essay':essay}
    return render(request, 'src/view_essay.html' , context)

