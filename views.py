from django.shortcuts import redirect, render

from .models import hello

from .froms import helloform

# Create your views here.


def home(request):

    form = helloform

    student = hello.objects.all

    return render(request, "home.html", {'form': form, 'student': student})


def add(request):

    form = helloform(request.POST)

    form.save()

    return redirect('/')


def edit(request, id):
    student = hello.objects.get(id=id)
    return render(request, "edit.html", {'student': student})


def update(request, id):
    student = hello.objects.get(id=id)
    form = helloform(request.POST, instance=student)
    form.save()
    return redirect('/')


def delete(request, id):
    student = hello.objects.get(id=id)
    student.delete()
    return redirect('/')
