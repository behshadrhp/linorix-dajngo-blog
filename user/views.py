from django.shortcuts import render
from .models import Profile, Skill
from blog.models import Essay

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
