from django.contrib import admin
from .models import Doctor, Patient, Appointment
import uuid

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('p_id', 'name', 'age', 'gender', 'phone', 'email')
    readonly_fields = ('p_id',)

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialization', 'experience')

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'appointment_date', 'appointment_time')
