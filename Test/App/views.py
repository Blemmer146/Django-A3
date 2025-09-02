from django.shortcuts import render

# Create your views here.
def Show(request):
    return render(request,'testapp/index.html')