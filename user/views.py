from django.shortcuts import render, redirect
from .models import Profile, Skill
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import ReCaptchaForm, RegisterForm, UpdateInformationForm, SkillForm
from validate_email_address import validate_email
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
import re

# Create your views here.


def user(request):
    # This function is for profile user

    # user
    users = Profile.objects.all()

    # pagination 
    paginator = Paginator(users, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    pagination = page_obj

    context = {'users': page_obj, 'pagination':pagination}
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

        username_invalid = request.POST['username']
        password = request.POST['password']
        captcha = ReCaptchaForm(request.POST)
        
        # username is valid - remove special character
        username = re.sub(r"[^a-zA-Z0-9]","",username_invalid)

        user = authenticate(username=username.lower(),password=password)
        
        if captcha.is_valid():
            if user is not None:
                login(request, user)
                messages.success(request, f'Login {user.username} is SuccessFull')
                return redirect(request.GET['next'] if 'next' in request.GET else 'account')
            else:
                messages.info(request, 'Invalid username or password')
                return redirect('login')
        
    else:
        captcha = ReCaptchaForm()
        

    
    context = {'captcha':captcha}
    return render(request, 'src/login.html', context)


def user_register(request):
    # This function is Register in Linorix
    register = RegisterForm()
    captcha = ReCaptchaForm()

    if request.method == 'POST':
        register = RegisterForm(request.POST)
        captcha = ReCaptchaForm(request.POST)     
        email = request.POST['email'].lower()

        # is valid email or not
        email_isvalid = validate_email(email, verify=True)

        # Username conf-edit
        username_invalid = request.POST['username']
        # username is valid - remove special character
        username = re.sub(r"[^a-zA-Z0-9]","",username_invalid)

        try:
            if email_isvalid:
                if captcha.is_valid():
                    if register.is_valid():
                        # create save space 
                        user = register.save(commit=False)
                        # change user name to lower
                        user.username = username.lower()
                        # save
                        user.save()
                        
                        login(request, user)
                        messages.success(request, f'Registration {user.username} was successful')

                        return redirect('account')
                    else:
                        messages.error(request, 'The system has a problem. please try again later')
                        return redirect('register')
            else:
                messages.error(request, 'The email is invalid. enter another email')

        except:
            messages.error(request, 'The system has a problem. please try again later')
            return redirect('register')
        


    context = {'register':register, 'captcha':captcha}
    return render(request, 'src/register.html', context)


def user_logout(request):
    # this function is for logout user
    
    logout(request)
    messages.info(request, 'User logged out successfully')
    return redirect('index')


@login_required(login_url='login')
def user_account(request):
    # This class is for account -- add or edit personal information

    users = request.user.profile

    # Skills
    top_skill = users.skill_set.exclude(description='')
    other_skill = users.skill_set.filter(description='')
    
    context = {'users': users, 'top_skill': top_skill,
               'other_skill': other_skill}
    return render(request, 'src/account.html', context)


@login_required(login_url='login')
def update_profile(request):
    # This function is for update profile information
    user = request.user.profile

    if request.method == 'POST':
        form = UpdateInformationForm(request.POST, request.FILES, instance=user)
        
        # save profile 
        if form.is_valid():
            form.save()
            return redirect('account')
    else:
        form = UpdateInformationForm(instance=user)


    context = {'form':form}
    return render(request, 'src/update.html', context)

@login_required(login_url='login')
def create_skill(request):
    # This function is for create skills

    owner = request.user.profile

    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.owner = owner
            skill.save()
            return redirect('account')
    else:
        form = SkillForm()
    
    context = {'form':form}
    return render(request, 'src/update.html', context)


@login_required(login_url='login')
def update_skill(request, pk):
    # This function is for update skills

    owner = request.user.profile
    skill = owner.skill_set.get(id=pk)

    if request.method == 'POST':
        form = SkillForm(request.POST,instance=skill)
        if form.is_valid():
            form.save()
            return redirect('account')
    else:
        form = SkillForm(instance=skill)


    context = {'form':form}
    return render(request, 'src/update.html', context)

@login_required(login_url='login')
def delete_skill(request, pk):
    # This function is for delete skills
    
    owner = request.user.profile
    skill = owner.skill_set.get(id=pk)

    if request.POST.get('delete') :
        # delete essay  
        skill.delete()
        return redirect('account')

    elif request.POST.get('cancel'):
        # cancel and back home page
        return redirect('account')
    
    context = {'form':skill}
    return render(request, 'src/delete.html', context)

