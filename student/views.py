from django.shortcuts import render, get_object_or_404, redirect
from .models import Student
from .forms import StudentForm

# View to display list of all students
def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})

# View to display details of a single student
def student_detail(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    return render(request, 'students/student_detail.html', {'student': student})

# View to add a new student
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