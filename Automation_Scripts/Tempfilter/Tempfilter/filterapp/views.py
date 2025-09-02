from django.shortcuts import render
from filterapp.form import Student_Regis
from .models import StuModel


# Create your views here.
def Student_Operation(request):
    if request.method=='POST':
        form=Student_Regis(request.POST)
        if form.is_valid():
            form.save(commit=True)
    else:
        form = Student_Regis()
    return render(request,'testapp/index.html',{'form':form})

def Student_List(request):
    stu_list = StuModel.objects.all()
    data = {
        'data': stu_list,
    }
    return render(request, 'testapp/student_list.html', data)
