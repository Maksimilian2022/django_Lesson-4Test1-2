from django.views.generic import ListView
from django.shortcuts import render

from .models import Student, Teacher
from django.http import HttpResponse

def students_list(request):
    ordering = 'group'
    template = 'school/students_list.html'
    context = {}
    search_students = Student.objects.all()
    student_info = [info for info in search_students]
    context = {"student_info": student_info}
    return render(request, template, context)
    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by

