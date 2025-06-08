from django.shortcuts import render
from .models import Contact, Project, Category

# Home Page - Show limited latest projects
def home(request):
    projects = Project.objects.all().order_by('-date_added')[:6]  # Latest 6 projects
    categories = Category.objects.all()  # ✅ Updated here
    return render(request, 'home.html', {'projects': projects, 'categories': categories})

# Full Projects Page
def projects(request):
    all_projects = Project.objects.all().order_by('-date_added')
    categories = Category.objects.all()  # ✅ Updated here
    return render(request, 'project.html', {'projects': all_projects, 'categories': categories})

# Contact Form Submission
def contact(request):
    if request.method == "POST":
        Contact.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            subject=request.POST['subject'],
            message=request.POST['message']
        )
        return render(request, 'contact_thankyou.html')  # Better UX to show success message
    return render(request, 'home.html')
from django.shortcuts import render
from .models import Contact, Project, Category

# Home Page - Show limited latest projects
def home(request):
    projects = Project.objects.all().order_by('-date_added')[:6]  # Latest 6 projects
    categories = Category.objects.all()  # ✅ Updated here
    return render(request, 'home.html', {'projects': projects, 'categories': categories})

# Full Projects Page
def projects(request):
    all_projects = Project.objects.all().order_by('-date_added')
    categories = Category.objects.all()  # ✅ Updated here
    return render(request, 'project.html', {'projects': all_projects, 'categories': categories})

# Contact Form Submission
def contact(request):
    if request.method == "POST":
        Contact.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            subject=request.POST['subject'],
            message=request.POST['message']
        )
        return render(request, 'contact_thankyou.html')  # Better UX to show success message
    return render(request, 'home.html')
