from django.shortcuts import render, redirect
from .models import Essay
from .forms import EssayForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    # This function is for developing and making changes to the index file

    essay = Essay.objects.all()

    context = {'essay': essay}
    return render(request, 'src/index.html', context)


@login_required(login_url='login')
def essay(request):
    # this function is for creating and changing and developing essay .

    owner = request.user.profile
    form = EssayForm

    if request.method == 'POST':
        form = form(request.POST, request.FILES)
        if form.is_valid():
            # create new Essay
            essay = form.save(commit=False)
            essay.owner = owner
            essay.save()
            return redirect('index')

    context = {'form': form}
    return render(request, 'src/new_essay.html', context)


def view_essay(request, pk):
    # This function is for developing and making changes to the view essay file

    essay = Essay.objects.get(slug=pk)

    context = {'essay': essay}
    return render(request, 'src/view_essay.html', context)


@login_required(login_url='login')
def update_essay(request, pk):
    # This function is for update essay form

    owner = request.user.profile
    essay = owner.essay_set.get(slug=pk)

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


@login_required(login_url='login')
def delete_essay(request, pk):
    # This function is for delete essay

    owner = request.user.profile
    essay = owner.essay_set.get(slug=pk)

    if request.POST.get('delete') :
        # delete essay  
        essay.delete()
        return redirect('index')

    elif request.POST.get('cancel'):
        # cancel and back home page
        return redirect('index')
    
    context = {'essay':essay}
    return render(request, 'src/delete_essay.html', context)
