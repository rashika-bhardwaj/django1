from django.shortcuts import render
from .forms import StudentRegistration
from .models import User
# Create your views here.
def show(request):
    # fm = StudentRegistration()
    # return render(request,'testapp/addcontent.html',{'form': fm})

    if request.method=='POST':
        fm = StudentRegistration()
        if fm.is_valid():
            # fm.save()
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            password = fm.cleaned_data['password']
            reg = User(name=name,email=email,password=password)
            reg.save()
    else:
        fm = StudentRegistration()
    stud = User.objects.all()
    return render(request,'testapp/addcontent.html',{'form': fm, 'stu':stud})
