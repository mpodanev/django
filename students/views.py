# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

# Views for Students

def students_list(request):
    students = (
        {'id': 1,
	 'first_name': u'Михайло',
	 'last_name': u'Поданев',
	 'ticket': 2123,
	 'image': 'img/Michel.JPG'},
        {'id': 2,
	 'first_name': u'Елон',
	 'last_name': u'Маск',
	 'ticket': 4523,
	 'image': 'img/Musk.jpg'},
        {'id': 3,
	 'first_name': u'Марк',
	 'last_name': u'Цукерберг',
	 'ticket': 2648,
	 'image': 'img/Zuckerberg.jpg'},
        {'id': 4,
	 'first_name': u'Стів',
	 'last_name': u'Джобс',
	 'ticket': 1254,
	 'image': 'img/jobs.jpg'})
    return render(request, 'students/students_list.html', {'students': students})

def students_add(request):
    return HttpResponse('<h1>Student Add Form</h1>')

def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)

def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)

# Views for Groups

def groups_list(request):
    return HttpResponse('<h1>Groups Listing</h1>')

def groups_add(request):
    return HttpResponse('<h1>Group Add Form</h1>')

def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Group %s</h1>' % gid)

def groups_delete(request, gid):
    return HttpResponse('<h1>Delete Group %s</h1>' % gid)
