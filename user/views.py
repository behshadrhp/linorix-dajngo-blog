from django.shortcuts import render, redirect
from .models import Profile, Skill
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.


def user(request):
    # This function is for profile user

    # user
    users = Profile.objects.all()

    context = {'users': users}
    return render(request, 'src/user.html', context)


def user_profile(request, pk):
    # This function is for view user profile

    # username filter
    users = Profile.objects.get(username=pk)

    # Skills
    top_skill = users.skill_set.exclude(description='')
    other_skill = users.skill_set.filter(description='')
    
    context = {'users': users, 'top_skill': top_skill,
               'other_skill': other_skill}
    return render(request, 'src/profile.html', context)


def user_login(request):
    # This function is for login user

    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username,password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'Login {user.username} is SuccessFull')
            return redirect(f'/users/author/{user.username}')
        else:
            messages.info(request, 'Invalid username or password')
            return redirect('login')


    return render(request, 'src/login_logout.html')


def user_logout(request):
    # this function is for logout user
    
    logout(request)
    messages.info(request, 'User logged out successfully')
    return redirect('index')
