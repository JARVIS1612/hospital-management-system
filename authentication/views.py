from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from .models import Doctors, Pharma, Users
from django.contrib.auth.hashers import make_password
from disease_checker.models import Diseases, Departments
from AppointmentBooking.models import Bookings, TimeSlots
from datetime import date


# Create your views here.
def signin(request):
    error = ''
    if request.method == 'POST':
        uname = request.POST['username']
        pwd = request.POST['password']
        user = authenticate(username=uname, password=pwd)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error = "Re-check Username/Password"

    return render(request, 'authentication/signin.html', {'error': error})


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        fname = request.POST['first_name']
        uname = request.POST['username']
        lname = request.POST['last_name']
        email = request.POST['email']
        num = request.POST['number']
        age = request.POST['age']
        gender = request.POST['gender']
        bd = request.POST['blood_group']
        pwd = request.POST['password1']
        is_patient = request.POST.get('is_patient', False)
        is_doctor = request.POST.get('is_doctor', False)
        is_pharma = request.POST.get('is_pharma', False)
        print(fname, lname, uname, email, num, age, gender, bd, pwd, is_pharma, is_doctor, is_patient)

        if (is_doctor and is_pharma and is_patient) or (is_doctor and is_pharma) or (is_doctor and is_patient) or (
                is_pharma and is_patient):
            error = "Select any one checkbox !!"
            return render(request, 'authentication/signup.html', {'form': form, 'error': error})

        elif form.is_valid():
            if is_doctor == "on":
                if request.POST.get('codeis_doctor', "ABC") == "i am doctor":
                    user = Users(first_name=fname, last_name=lname, password=make_password(pwd), username=uname,
                                 email=email, number=num, age=age,
                                 gender=gender, blood_group=bd, is_doctor=True, is_patient=False, is_pharma=False)
                    user.save()
                    d = Doctors(username=Users.objects.get(username=uname))
                    d.save()
                    return redirect('department')
                else:
                    error = "Special Code is wrong !!"
                    return render(request, 'authentication/signup.html', {'form': form, 'error': error})

            elif is_pharma == "on":
                if request.POST.get('codeis_pharma', "ABC") == "i am pharma":
                    user = Users(first_name=fname, last_name=lname, username=uname, password=make_password(pwd),
                                 email=email, number=num, age=age,
                                 gender=gender, blood_group=bd, is_doctor=False, is_patient=False, is_pharma=True)
                    user.save()
                    p = Pharma(username=Users.objects.get(username=uname))
                    p.save()
                    return redirect('signin')
                else:
                    error = "Special Code is wrong !!"
                    return render(request, 'authentication/signup.html', {'form': form, 'error': error})

            else:
                user = Users(first_name=fname, last_name=lname, username=uname, password=make_password(pwd),
                             email=email, number=num, age=age,
                             gender=gender, blood_group=bd, is_doctor=False, is_patient=True, is_pharma=False)
                user.save()
                return redirect('signin')
        else:
            print(form.errors)
        error = ""
    else:
        error = ""
        form = CustomUserCreationForm()

    return render(request, 'authentication/signup.html', {'form': form, 'error': error})


def signout(request):
    logout(request)
    return redirect('home')


def profile(request):
    dep = Doctors.objects.filter(username=request.user)
    bookings = Bookings.objects.filter(date=date.today(), is_checked=False, is_approved=True)
    if dep:
        return render(request, 'authentication/profile.html',
                      {"Department": dep[0].department.Departments, "bookings": bookings})
    else:
        return render(request, 'authentication/profile.html')


def department(request):
    error = ''
    if request.method == 'POST':
        uname = request.POST['username']
        pwd = request.POST['password']
        department_ = request.POST['dep']
        user = authenticate(username=uname, password=pwd)

        if user is not None:
            doc = Doctors.objects.get(username=uname)
            doc.department = Departments.objects.get(Departments=department_)
            doc.save()
            return redirect('signin')
        else:
            error = "Re-check Username/Password"
    dep = []
    for i in Departments.objects.all():
        dep.append(i.Departments)
    return render(request, 'authentication/department.html', {'dep': dep, 'error': error})


def update(request, id):
    booking = Bookings.objects.get(id=id)
    booking.is_checked = True
    booking.save()
    return redirect("profile")