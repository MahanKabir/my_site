from django.shortcuts import render, redirect
from .forms import CourseForm
from .models import Course


# Create your views here.
def create(request):
    if request.method == "POST":
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('read.course')
    return render(request, 'course/create.html')


def read(request):
    courses = Course.objects.all()
    return render(request, 'course/read.html', {'courses': courses})


def update(request, course_id):
    course = Course.objects.get(id=course_id)
    if request.method == "POST":
        form = CourseForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            form.save()
    return render(request, 'course/update.html', {'course': course})


def delete(request, course_id):
    course = Course.objects.get(id=course_id)
    course.delete()
    return redirect('read.course')
