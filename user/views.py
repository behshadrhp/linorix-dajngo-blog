from django.shortcuts import render
from .models import Profile

# Create your views here.

def user(request):
    # This function is for profile user

    users = Profile.objects.all()

    context = {'users':users}
    return render(request, 'src/user.html', context)

def user_profile(request, pk):
    # This function is for view user profile

    users = Profile.objects.get(username=pk)

    context = {'users':users}
    return render(request, 'src/profile.html', context)