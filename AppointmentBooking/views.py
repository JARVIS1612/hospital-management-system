from django.shortcuts import render, redirect
from .models import TimeSlots, Bookings
from authentication.models import Doctors, Users
from disease_checker.models import Departments
from datetime import *
import random
from django.db.models import Q
from django.core.mail import send_mail

# Create your views here.

def departmentlist(request):
    dep = []
    dis = [
        "Evaluate, monitor, and supervise patient care before, during, and after surgery, delivering anesthesia, leading the Anesthesia Care Team, and ensuring optimal patient safety. Physician anesthesiologists specialize in anesthesia care, pain management, and critical care medicine.",
        "Diagnosing and treating diseases of the heart, blood vessels, and circulatory system. These diseases include coronary artery disease, heart rhythm problems, and heart failure.",
        "Diagnosing and treating problems concerning patient's teeth and gums. They provide regular checkups and cleanings in addition to more detailed procedures like root canals or installing braces.",
        "Diagnoses, treats and manages disorders of the brain and nervous system (brain, spinal cord and nerves). A neurologist knows the anatomy, function and conditions that affect your nerves and nervous system.",
        "Diagnosis, treatment, prevention and rehabilitation of injuries, disorders and diseases of the body's musculoskeletal system.",
        "Using X-rays, magnetic waves and ultrasound to obtain detailed images of the inside of the body. Doctors can then use those images to detect and diagnose illnesses and injuries, as well as to help develop treatment plans.",
    ]
    for i in Departments.objects.all():
        dep.append(i.Departments)
    dict = []
    for i in range(len(dep)):
        dict.append([dep[i],dis[i]])
    return render(request, 'AppointmentBooking/departments.html', {'dict':dict})


def Appointment(request, department):
    dep = []
    for i in Departments.objects.all():
        dep.append(i.Departments)

    error = ""
    if request.method == "POST":
        des = request.POST['notes']
        t = request.POST['time']
        date_ = request.POST['date']
        depart = Departments.objects.get(Departments=department)
        time = TimeSlots.objects.get(time_slot=t)
        b = Bookings.objects.filter(username=request.user, date=date_, is_checked=False)
        print(b)
        if b:
            error = "You already booked this appointment"
        elif datetime.strptime(date_, '%Y-%m-%d').date() <= date.today():
            error = "Please enter future dates only"
        else:
            print(des, t, date_)
            ap = Bookings(username=request.user, department=depart, date=date_, time_slot=time, notes=des)
            ap.save()
            success = "Your Appointment request hase been sent... please wait for conformation email"
            return render(request, 'AppointmentBooking/appointment.html',
                          {'timeslots': TimeSlots.objects.all(), 'departments': dep, "success": success})

    return render(request, 'AppointmentBooking/appointment.html',
                  {'timeslots': TimeSlots.objects.all(), 'departments': dep, "error": error})


def Dashboard(request, booking_id=0):
    start_date = datetime.now().date()
    doctor = request.user
    department = Doctors.objects.get(username=doctor).department
    appointment = Bookings.objects.filter(Q(department=department), Q(is_checked=False), Q(is_approved=False),
                                          Q(date__gte=start_date)).order_by('date')
    if request.method == "POST":
        if booking_id != 0:
            time = request.POST['time']
            note = request.POST['notes']
            if time == "N/A":
                print("Removed")
            else:
                booking = Bookings.objects.get(id=booking_id)
                booking.assigned_doctor = Doctors.objects.get(username=request.user)
                booking.assigned_timeslot = TimeSlots(time_slot=time)
                booking.is_approved = True
                booking.unique_code = random.randint(10000, 99999)
                booking.save()
                # send_mail(
                #     "Your Appointment accepted",
                #     "Allocated Slot: "+str(time)+"\nName of Doctor: "+str(request.user)+"\nUnique Code: "+str(booking.unique_code),
                #     "vaibhavkundaliya7@gmail.com",
                #     ["vaibhavkundaliya7@gmail.com"]
                # )
                return redirect("dashboard")
        else:
            start_date = request.POST.get('start_date', False)
            if start_date:
                start_date = datetime.strptime(start_date, "%Y-%m-%d")
            else:
                start_date = datetime.now().date()
            end_date = request.POST.get('end_date', None)
            is_checked = request.POST.get('is_checked', False)
            is_approved = request.POST.get('is_approved', False)
            if is_checked:
                is_approved = True
            print(start_date, end_date, is_approved, is_checked)
            if end_date:
                end_date = datetime.strptime(end_date, "%Y-%m-%d")
                appointment = Bookings.objects.filter(Q(department=department), Q(is_checked=is_checked),
                                                      Q(is_approved=is_approved),
                                                      Q(date__gte=start_date), Q(date__lte=end_date)).order_by('date')
            else:
                appointment = Bookings.objects.filter(Q(department=department), Q(is_checked=is_checked),
                                                      Q(is_approved=is_approved), Q(date__gte=start_date)).order_by(
                    'date')
                print(appointment)

    return render(request, 'AppointmentBooking/dashboard.html',
                  {"BookingRequests": appointment, 'Time_slots': TimeSlots.objects.all()})
