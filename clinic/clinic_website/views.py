from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Doctor


# Registration view
def register(request):
    """
    Handles user registration. Displays a registration form and creates a new user if the form is valid.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = UserCreationForm()  # Instantiate an empty form for GET requests
    return render(request, 'registration/register.html', {'form': form})


# Login view
def user_login(request):
    """
    Handles user login. Displays a login form and authenticates the user if the form is valid.
    """
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirect to the home page after successful login
    else:
        form = AuthenticationForm()  # Instantiate an empty form for GET requests
    return render(request, 'registration/login.html', {'form': form})


# Home view
@login_required
def home(request):
    """
    Displays the home page. Requires the user to be logged in.
    """
    return render(request, 'home.html', {'user': request.user})


# Logout view
@login_required
def user_logout(request):
    """
    Logs out the user and redirects to the landing page.
    """
    logout(request)
    return redirect('landing')  # Redirect to the landing page after logout


# Search view
def search(request):
    """
    Handles search functionality. Filters doctors based on specialization and area.
    """
    specialization = request.GET.get('specialization')  # Get specialization from query parameters
    area = request.GET.get('area')  # Get area from query parameters
    doctors = Doctor.objects.filter(specialization=specialization, area=area)  # Filter doctors based on search criteria
    return render(request, 'search_results.html', {'doctors': doctors})


# Doctor detail view
def doctor_detail(request, doctor_id):
    """
    Displays details of a specific doctor. Retrieves the doctor based on the provided ID.
    """
    doctor = get_object_or_404(Doctor, id=doctor_id)  # Get the doctor or return a 404 if not found
    return render(request, 'doctor_detail.html', {'doctor': doctor})


# Base view
def base(request):
    """
    Renders the base template. Can be used as a common layout for other views.
    """
    return render(request, 'base.html')


# Landing page view
def landing(request):
    """
    Renders the landing page.
    """
    return render(request, 'index.html')
