from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request, 'testapp/homepage.html')
def Movie(request):
    return render(request, 'testapp/movie.html')
def Sports(request):
    return render(request, 'testapp/sports.html')
def News(request):
    return render(request, 'testapp/news.html')