from django import forms
from django.forms import ModelChoiceField

from api.apps.companies.models import Company
from api.apps.gdrive.models import Timetable


class TimetableForm(forms.ModelForm):
    company = ModelChoiceField(queryset=Company.objects.all(), to_field_name='slug', label="Operadora de transportes")

    class Meta:
        model = Timetable
        fields = ('company', 'map_data',)
