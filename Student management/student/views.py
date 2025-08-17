from django.http import HttpResponse
from .forms import StudentForm
from .models import Student
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseForbidden

# Create view.
@login_required
def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.user = request.user
            student.save()
            return redirect('thank_you')  # redirect here
    else:
        form = StudentForm()
    return render(request, 'student/create.html', {'form': form})

# update view
@login_required
def update_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    
    # Check ownership
    if student.user != request.user:
        return HttpResponseForbidden("You are not allowed to edit this record.")
    
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = StudentForm(instance=student)
        
    return render(request, 'student/update.html', {'form': form})
# delete view
@login_required
def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if not request.user.is_staff:
        return HttpResponseForbidden("Only staff can delete records.")
    
    # proceed with deletion if staff
    if request.method == 'POST':
        student.delete()
        return redirect('list')
    
    return render(request, 'student/confirm_delete.html', {'student': student})

@login_required
def student_list(request):
    students = Student.objects.all
    return render(request, 'student/list.html', {'students': students})

@login_required
def thank_you(request):
    return render(request, 'student/thank_you.html')