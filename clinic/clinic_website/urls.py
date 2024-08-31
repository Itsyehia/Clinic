from django.urls import path
from . import views
from .views import register, user_login, home, search, doctor_detail, landing, base, user_logout

urlpatterns = [
    # Route for user registration
    path('register/', register, name='register'),

    # Route for user login
    path('login/', user_login, name='login'),

    # Route for landing page (home page or welcome page)
    path('', landing, name='landing'),

    # Route for the home page, accessible only after login
    path('home/', home, name='home'),

    # Route for search functionality
    path('search/', search, name='search'),

    # Route to view details of a specific doctor, identified by doctor_id
    path('doctor/<int:doctor_id>/', doctor_detail, name='doctor_detail'),

    # Route for the base template, typically used for layout purposes
    path('base/', base, name='base'),

    # Redundant route for landing page (already defined above as the root route)
    path('landing/', landing, name='landing'),

    # Route for user logout
    path('logout/', user_logout, name='logout'),
]
