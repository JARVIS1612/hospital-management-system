from django.shortcuts import render, HttpResponse
from disease_checker.detect_lung_cancer import detect_lung_cancer_
from disease_checker.detect_skin_disease import detect_skin_disease_
from disease_checker.detect_diabeties import detect_diabeties_
from django.core.files.storage import FileSystemStorage


# Create your views here.
def lung_cancer(request):
    result = []
    filepath = ""
    if request.method == "POST":
        img = request.FILES['img']
        fs = FileSystemStorage()
        fileurl = fs.save(img.name, img)
        filepath = fs.url(fileurl)
        print(filepath)
        result = detect_lung_cancer_(filepath)
    return render(request, 'disease_checker/lung_cancer.html', {'result': result, 'img': filepath})


def skin_disease(request):
    result = []
    filepath = ""
    if request.method == "POST":
        img = request.FILES['img']
        fs = FileSystemStorage()
        fileurl = fs.save(img.name, img)
        filepath = fs.url(fileurl)
        print(filepath)
        result = detect_skin_disease_(filepath)
    return render(request, 'disease_checker/skin_disease.html', {'result': result, 'img': filepath})


def brain_tumor(request):
    return render(request, 'disease_checker/brain_tumor.html')


def diabetes(request):
    if request.method == "POST":
        lis = []
        for i in range(15):
            temp = request.POST[str(i)]
            lis.append(int(temp))
        weight = float(request.POST['16'])
        height = float(request.POST['15'])/100
        BMI = weight / height ** 2
        if BMI >= 30:
            lis.append(1)
        else:
            lis.append(0)
        print(lis)
        result = detect_diabeties_(lis)
        print(result)
        return render(request, 'disease_checker/diabetes.html', {'result': result+1})

    return render(request, 'disease_checker/diabetes.html', {'result': False})


def pneumonia(request):
    return render(request, 'disease_checker/pneumonia.html')
