from django import forms
from .models import Attendance
from datetime import date
from .models import Boxer

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['boxer', 'date', 'is_present', 'is_excused']
        widgets = {
            'date': forms.SelectDateWidget(),
        }


class BoxerForm(forms.ModelForm):
    class Meta:
        model = Boxer
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter boxer name'})
        }

class MultiAttendanceForm(forms.Form):
    date = forms.DateField(widget=forms.SelectDateWidget())

    def __init__(self, *args, **kwargs):
        boxers = kwargs.pop('boxers')
        super().__init__(*args, **kwargs)
        self.boxers = boxers

        for boxer in boxers:
            self.fields[f'present_{boxer.id}'] = forms.BooleanField(
                required=False,
                label='',
                widget=forms.CheckboxInput()
            )
            self.fields[f'excused_{boxer.id}'] = forms.BooleanField(
                required=False,
                label='',
                widget=forms.CheckboxInput()
            )


class DateSelectionForm(forms.Form):
    DATE_CHOICES = sorted(
        {a.date for a in Attendance.objects.all()},
        reverse=True
    )
    date = forms.ChoiceField(
        choices=[(d.strftime('%Y-%m-%d'), d.strftime('%Y-%m-%d')) for d in DATE_CHOICES],
        label="Select a date",
        widget=forms.Select(attrs={'class': 'form-control'})
    )