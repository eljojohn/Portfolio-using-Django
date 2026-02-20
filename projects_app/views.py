from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Project
from accounts_app.models import Profile


# ==============================
# HOME PAGE (Portfolio Landing)
# ==============================
from accounts_app.models import Profile
from .models import Project

def home(request):

    # latest 3 projects for homepage
    projects = Project.objects.all().order_by('-created_date')[:3]

    # portfolio profile (bio + image)
    profile = Profile.objects.first()

    return render(request, 'home.html', {
        'projects': projects,
        'profile': profile
    })


# ==============================
# PUBLIC - ALL PROJECTS PAGE
# ==============================
def project_list(request):

    projects = Project.objects.all().order_by('-created_date')

    return render(request, 'projects.html', {
        'projects': projects
    })


# ==============================
# PUBLIC - SINGLE PROJECT
# ==============================
def project_detail(request, slug):

    project = get_object_or_404(Project, slug=slug)

    return render(request, 'project_detail.html', {
        'project': project
    })


# ==============================
# DASHBOARD (LOGIN REQUIRED)
# ==============================
@login_required
def dashboard(request):

    projects = Project.objects.all().order_by('-created_date')

    return render(request, 'dashboard.html', {
        'projects': projects
    })


# ==============================
# ADD PROJECT (ADMIN ONLY)
# ==============================
@login_required
def project_add(request):

    if not request.user.is_superuser:
        return HttpResponseForbidden("Only admin can add projects")

    if request.method == "POST":

        Project.objects.create(
            title=request.POST.get('title'),
            description=request.POST.get('description'),
            tech_stack=request.POST.get('tech_stack'),
            github_link=request.POST.get('github_link'),
            live_demo_link=request.POST.get('live_demo_link'),
        )

        return redirect('dashboard')

    return render(request, 'project_add.html')


# ==============================
# EDIT PROJECT (ADMIN ONLY)
# ==============================
@login_required
def project_edit(request, slug):

    if not request.user.is_superuser:
        return HttpResponseForbidden("Only admin can edit projects")

    project = get_object_or_404(Project, slug=slug)

    if request.method == "POST":

        project.title = request.POST.get('title')
        project.description = request.POST.get('description')
        project.tech_stack = request.POST.get('tech_stack')
        project.github_link = request.POST.get('github_link')
        project.live_demo_link = request.POST.get('live_demo_link')

        project.save()

        return redirect('dashboard')

    return render(request, 'project_edit.html', {
        'project': project
    })


# ==============================
# DELETE PROJECT (ADMIN ONLY)
# ==============================
@login_required
def project_delete(request, slug):

    if not request.user.is_superuser:
        return HttpResponseForbidden("Only admin can delete projects")

    project = get_object_or_404(Project, slug=slug)

    if request.method == "POST":
        project.delete()

    return redirect('dashboard')
