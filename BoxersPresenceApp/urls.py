from django.urls import path
from . import views

from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('', lambda request: redirect('mark_attendance', permanent=False)),
    path('mark/', views.mark_attendance, name='mark_attendance'),
    path('list/', views.attendance_list, name='attendance_list'),
    path('boxers/', views.boxer_list, name='boxer_list'),
    path('delete-boxer/<int:boxer_id>/', views.delete_boxer, name='delete_boxer'),
    path('boxer-report/<int:boxer_id>/', views.boxer_report, name='boxer_report'),
    path('attendance/delete/<int:attendance_id>/', views.delete_attendance, name='delete_attendance'),
    path('attendance-by-date/', views.attendance_by_date, name='attendance_by_date'),
    path('summary/', views.attendance_summary, name='attendance_summary'),
]
