from django.shortcuts import render, HttpResponseRedirect
from .forms import SignUpForm, UserProfileForm
from django.contrib import messages
from .models import UserProfile
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout


# Home
def home(request):
    return render(request, 'enroll/home.html')

# Signup
def sign_up(request):
    user_form = SignUpForm()
    profile_form = UserProfileForm()
    if request.method == 'POST':
        user_form = SignUpForm(request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            login(request, user)

            messages.success(request, 'Account created successfully!')
            return HttpResponseRedirect('/profile/')
        else:
            user_form = SignUpForm()
            profile_form = UserProfileForm()

    return render(request, 'enroll/signup.html', {'user_form': user_form, 'profile_form': profile_form})

# Login Function
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in successfully !!')
                    return HttpResponseRedirect('/profile/')
        else:
            fm = AuthenticationForm()
        return render(request, 'enroll/userlogin.html', {'form': fm})
    else:
        return HttpResponseRedirect('/profile/')


# Profile
def user_profile(request):
    if request.user.is_authenticated:

        user_profile = UserProfile.objects.get(user=request.user)
        return render(request, 'enroll/profile.html', {'user_profile': user_profile})
    else:
        return HttpResponseRedirect('/login/')

# Logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')
