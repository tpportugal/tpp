from django import forms
from django.forms import ModelChoiceField, FileInput

from api.apps.agencies.models import Agency
from api.apps.gdrive.models import Timetable


class TimetableForm(forms.ModelForm):
    agency = ModelChoiceField(queryset=Agency.objects.all(), to_field_name='slug', label="Operadora de transportes")
    map_data = forms.FileField(widget=FileInput(attrs={'accept':'application/pdf,image/jpeg,image/png'}))

    class Meta:
        model = Timetable
        fields = ('agency', 'map_data',)
