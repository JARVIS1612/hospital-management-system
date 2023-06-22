import django

django.setup()

#set DJANGO_SETTINGS_MODULE=hospital-management-system.settings

from authentication.models import Doctors, Pharma, Users
from django.contrib.auth.hashers import make_password
from disease_checker.models import Departments
from AppointmentBooking.models import Bookings
# dep = ['Anesthesiology', 'Cardiology', 'Dentist', 'Neurology']  # , 'Orthopedics', 'Radiology']
#
# user = Users(first_name="doctor", last_name="doctor",
#              password=make_password("vk@16122001"),
#              username="doc7@123",
#              email="doc7@gmail.com",
#              number=27,
#              age=45, gender="Male", blood_group="A+", is_doctor=True,
#              is_patient=False, is_pharma=False)
#
# d = Doctors(username=user, department=Departments.objects.get(Departments=dep[3]))
#
# user.save()
# d.save()

# doc = Doctors.objects.filter(department=Departments.objects.get(Departments=dep[0]))
# print(doc)

# b = Bookings.objects.filter(username=request.user, date=date, is_checked=False)
# print(b)

# import datetime
# start_date = datetime.datetime.now().date()
# # start_date = start_date.strftime("%Y-%m-%d")
# end_date = None
# print((start_date))

# import cv2
# import matplotlib.pyplot as plt
#
# img = cv2.imread("./media/img_n_YnoidiV.png")
# # cv2.imshow("img",img)
# print(img.shape)