import uuid

from django.http import HttpResponse
from django.shortcuts import render, redirect

from api.apps.gdrive.forms import TimetableForm
from api.apps.gdrive.models import Timetable


def upload_timetable(request):
    if request.method == 'POST':
        form = TimetableForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("Obrigado pelo upload!")
    else:
        form = TimetableForm()
    return render(request, 'timetable_upload.html', {
        'form': form
    })
