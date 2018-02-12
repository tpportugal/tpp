from django import forms
from django.forms import ModelChoiceField, FileInput

from api.models.gtfs.agencies.models import Agency
from api.models.gdrive.models import Timetable


class TimetableForm(forms.ModelForm):
    agency = ModelChoiceField(queryset=Agency.objects.all(), to_field_name='slug', label="Operadora de transportes")
    map_data = forms.FileField(widget=FileInput(attrs={'accept':'application/pdf,image/jpeg,image/png'}))

    class Meta:
        model = Timetable
        fields = ('agency', 'map_data',)
