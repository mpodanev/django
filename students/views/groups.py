# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

# Views for Groups

def groups_list(request):
    groups = (
		{'id': 1,
	 'full_name': u'Поданев Михайло',
	 'group': u'МтМ-21'},
	 	{'id': 2,
	 'full_name': u'Маск Елон',
	 'group': u'МтМ-22'},
	 	{'id': 3,
	 'full_name': u'Цукерберг Марк',
	 'group': u'МтМ-23'},
	 	{'id': 4,
	 'full_name': u'Джобс Стів',
	 'group': u'МтМ-24'})
    return render(request,'groups/groups_list.html', {'groups': groups})

def groups_add(request):
    return HttpResponse('<h1>Group Add Form</h1>')

def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Group %s</h1>' % gid)

def groups_delete(request, gid):
    return HttpResponse('<h1>Delete Group %s</h1>' % gid)