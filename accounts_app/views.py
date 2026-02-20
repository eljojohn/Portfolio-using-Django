from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from projects_app.models import Project


# ======================
# SIGNUP VIEW
# ======================
def signup_view(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # check existing user
        if User.objects.filter(username=username).exists():
            return render(request, 'registration/signup.html', {
                'error': 'Username already exists'
            })

        # create user
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        login(request, user)
        return redirect('dashboard')

    return render(request, 'registration/signup.html')


# ======================
# LOGIN VIEW
# ======================
def login_view(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'registration/login.html', {
                'error': 'Invalid credentials'
            })

    return render(request, 'registration/login.html')


# ======================
# LOGOUT VIEW
# ======================
def logout_view(request):
    logout(request)
    return redirect('login')


# ======================
# DASHBOARD VIEW
# ======================
@login_required
def dashboard_view(request):

    projects = Project.objects.all().order_by('-created_date')

    return render(request, 'dashboard.html', {
        'projects': projects
    })
