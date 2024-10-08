"""
URL configuration for student_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from student import views


# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', views.student_list, name='student_list'),  # List of all students
#     path('<int:student_id>/', views.student_detail, name='student_detail'),  # Student detail
#     path('new/', views.student_create, name='student_create'),  # Add a new student
#     path('<int:student_id>/edit/', views.student_edit, name='student_edit'),  # Edit student details
#     path('students/delete/<int:student_id>/', views.delete_student, name='delete_student'),
#     path('accounts/', include('django.contrib.auth.urls')),  # Includes login, logout, password reset views
#     path('', include('student_management.urls')),  # Replace 'your_app' with your actual app name
# ]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.student_list, name='student_list'),  # List of all students
    path('<int:student_id>/', views.student_detail, name='student_detail'),  # Student detail
    path('new/', views.student_create, name='student_create'),  # Add a new student
    path('<int:student_id>/edit/', views.student_edit, name='student_edit'),  # Edit student details
    path('students/delete/<int:student_id>/', views.delete_student, name='delete_student'),
    path('accounts/', include('django.contrib.auth.urls')),  # Includes login, logout, password reset views
    
]