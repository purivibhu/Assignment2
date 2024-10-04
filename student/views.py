from django.shortcuts import render, get_object_or_404, redirect
from .models import Student
from .forms import StudentForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.core.paginator import Paginator


# View to display list of all students
@login_required
def student_list(request):
    query = request.GET.get('q')  # Get the search query from the request
    if query:
        students = Student.objects.filter(
            first_name__icontains=query  # Filter by first name
        ) | Student.objects.filter(
            last_name__icontains=query  # Filter by last name
        )
    else:
        students = Student.objects.all()  # Show all students if no query

    # Set up pagination
    paginator = Paginator(students, 5)  # Show 5 students per page
    page_number = request.GET.get('page')  # Get the page number from the request
    page_obj = paginator.get_page(page_number)  # Get the page object

    return render(request, 'students/student_list.html', {'page_obj': page_obj})

# View to display details of a single student
@login_required
def student_detail(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    return render(request, 'students/student_detail.html', {'student': student})

# View to add a new student
@login_required
def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'students/student_form.html', {'form': form})

# View to edit an existing student
@login_required
def student_edit(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_detail', student_id=student.id)
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/student_form.html', {'form': form})

@login_required
def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'student_confirm_delete.html', {'student': student})