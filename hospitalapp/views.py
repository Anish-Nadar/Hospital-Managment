from datetime import datetime, time, timedelta
from django.shortcuts import render, redirect
from .forms import AppointmentForm, PatientForm
from .models import Appointment
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
def index(request):
    return render(request, 'index.html')

def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            date = form.cleaned_data['appointment_date']
            doctor = form.cleaned_data['doctor']

            # Get all appointments for this doctor on that date
            existing = Appointment.objects.filter(doctor=doctor, appointment_date=date).order_by('appointment_time')

            # Generate available time slots from 9:00 AM to 6:00 PM
            start = datetime.combine(date, time(9, 0))
            slots = [start + timedelta(minutes=30 * i) for i in range(18)]  # 18 slots of 30 mins

            # Get list of already booked times
            booked_times = [datetime.combine(date, appt.appointment_time) for appt in existing]

            # Find the first available slot
            available_slot = None
            for slot in slots:
                if slot not in booked_times:
                    available_slot = slot.time()
                    break

            if available_slot:
                appointment.appointment_time = available_slot
                appointment.save()
                return render(request, 'appointment-success.html', {'appointment': appointment})
            else:
                messages.error(request, "No available slots for this doctor on the selected date.")
    else:
        form = AppointmentForm()

    return render(request, 'book_appointment.html', {'form': form})

def register_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Patient registered successfully!')
            return redirect('registration_success')
    else:
        form = PatientForm()
    return render(request, 'register_patient.html', {'form': form})
from django.shortcuts import render
from .models import Doctor

def doctors_list(request):
    specialization = request.GET.get('specialization')
    experience = request.GET.get('experience')

    doctors = Doctor.objects.all()

    if specialization:
        doctors = doctors.filter(specialization__icontains=specialization)
    if experience:
        doctors = doctors.filter(experience__gte=experience)

    return render(request, 'doctors_list.html', {'doctors': doctors})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            uname = form.cleaned_data.get('username')
            pwd = form.cleaned_data.get('password')
            user = authenticate(username=uname, password=pwd)
            if user is not None:
                login(request, user)
                return redirect('home')  # Change to wherever you want to redirect after login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def registration_success(request):
    return render(request, 'registration_success.html')