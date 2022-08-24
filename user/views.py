from django.shortcuts import render
from .models import Profile

# Create your views here.

def user(request):
    # This function is for profile user

    users = Profile.objects.all()

    context = {'users':users}
    return render(request, 'src/user.html', context)