from datetime import datetime

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse

from .forms import BoxerForm, DateSelectionForm

from django.shortcuts import render, redirect
from .models import Boxer, Attendance

def attendance_list(request):
    attendance_records = Attendance.objects.all().order_by('-date')
    return render(request, 'BoxersPresenceApp/attendance_list.html', {
        'attendance_records': attendance_records
    })

def delete_boxer(request, boxer_id):
    boxer = get_object_or_404(Boxer, id=boxer_id)
    boxer.delete()
    return HttpResponseRedirect(reverse('boxer_list'))

def boxer_list(request):
    boxers = Boxer.objects.all()
    form = BoxerForm()

    if request.method == 'POST' and 'add_boxer' in request.POST:
        form = BoxerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('boxer_list')

    return render(request, 'BoxersPresenceApp/boxer_list.html', {
        'boxers': boxers,
        'form': form,
    })
def boxer_report(request, boxer_id):
    boxer = get_object_or_404(Boxer, id=boxer_id)
    records = Attendance.objects.filter(boxer=boxer).order_by('-date')

    total = records.count()
    present_count = records.filter(is_present=True).count()
    absent_count = total - present_count

    excused_absences = records.filter(is_present=False, is_excused=True).count()
    unexcused_absences = records.filter(is_present=False, is_excused=False).count()

    def percentage(part, whole):
        return round((part / whole) * 100, 2) if whole else 0

    context = {
        'boxer': boxer,
        'records': records,
        'total': total,
        'present_pct': percentage(present_count, total),
        'absent_pct': percentage(absent_count, total),
        'excused_pct': percentage(excused_absences, absent_count),
        'unexcused_pct': percentage(unexcused_absences, absent_count),
    }

    return render(request, 'BoxersPresenceApp/boxer_report.html', context)


def mark_attendance(request):
    boxers = Boxer.objects.all()

    if request.method == 'POST':
        date = request.POST.get('date')
        total = int(request.POST.get('total_boxers'))

        for i in range(1, total + 1):
            boxer_id = request.POST.get(f'boxer_id_{i}')
            attendance = request.POST.get(f'attendance_{i}')
            excused = request.POST.get(f'excused_{i}') == 'on'

            if boxer_id and attendance:
                Attendance.objects.create(
                    boxer_id=boxer_id,
                    date=date,
                    is_present=(attendance == 'Present'),
                    is_excused=excused
                )
        return redirect('attendance_list')

    return render(request, 'BoxersPresenceApp/mark_attendance.html', {'boxers': boxers})

def delete_attendance(request, attendance_id):
    attendance = get_object_or_404(Attendance, id=attendance_id)
    attendance.delete()
    return redirect('attendance_list')  # Or wherever you want to return


def attendance_by_date(request):
    form = DateSelectionForm()
    present_boxers = None

    if request.method == 'POST':
        form = DateSelectionForm(request.POST)
        if form.is_valid():
            selected_date_str = form.cleaned_data['date']
            selected_date = datetime.strptime(selected_date_str, '%Y-%m-%d').date()
            present_boxers = Attendance.objects.filter(date=selected_date, is_present=True)

    return render(request, 'BoxersPresenceApp/attendance_by_date.html', {
        'form': form,
        'present_boxers': present_boxers
    })

def attendance_summary(request):
    summary = []

    for boxer in Boxer.objects.all():
        total = Attendance.objects.filter(boxer=boxer).count()
        present = Attendance.objects.filter(boxer=boxer, is_present=True).count()
        absent = Attendance.objects.filter(boxer=boxer, is_present=False).count()
        excused = Attendance.objects.filter(boxer=boxer, is_present=False, is_excused=True).count()

        percent_present = round((present / total) * 100, 2) if total > 0 else 0
        percent_excused = round((excused / absent) * 100, 2) if absent > 0 else 0

        summary.append({
            'name': boxer.name,
            'present': percent_present,
            'excused': percent_excused,
        })

    return render(request, 'BoxersPresenceApp/attendance_summary.html', {'summary': summary})
