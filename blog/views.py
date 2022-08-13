from django.shortcuts import render, redirect
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
        form = form(request.POST, request.FILES)
        if form.is_valid():
            # create new Essay
            form.save()
            return redirect('index')

    context = {'form': form}
    return render(request, 'src/new_essay.html', context)


def view_essay(request, pk):
    # This function is for developing and making changes to the view essay file

    essay = Essays.objects.get(slug=pk)

    context = {'essay': essay}
    return render(request, 'src/view_essay.html', context)


def update_essay(request, pk):
    # This function is for update essay form

    essay = Essays.objects.get(slug=pk)

    # new instance
    form = EssayForm(instance=essay)

    if request.method == 'POST':
        form = EssayForm(request.POST, request.FILES, instance=essay )
        if form.is_valid():
            # update form
            form.save()
            return redirect('index')

    context = {'form': form}
    return render(request, 'src/new_essay.html', context)


def delete_essay(request, pk):
    # This function is for delete essay

    essay = Essays.objects.get(slug=pk)

    if request.POST.get('delete') :
        # delete essay
        essay.delete()
        return redirect('index')

    elif request.POST.get('cancel'):
        # cancel and back home page
        return redirect('index')
    
    context = {'essay':essay}
    return render(request, 'src/delete_essay.html', context)
