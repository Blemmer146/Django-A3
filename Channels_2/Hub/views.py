from django.shortcuts import render

# Create your views here.

def Home(request):
    head='Welcome to Hub Links'
    type='home'
    hm={
        'head': head,
        'type': type
    }
    return render(request, 'testapp/index.html', hm)
def Movie(request):
    Head = 'Welcome to Movie Portal'
    type = 'movie'
    mv={
        'head': Head,
        'type': type
    }
    return render(request, 'testapp/index.html', mv)
def Sports(request):
    Head = 'Welcome to Sports Portal'
    type = 'sports'
    sp = {
        'head': Head,
        'type': type
    }
    return render(request, 'testapp/index.html', sp)
def News(request):
    Head = 'Welcome to News Portal'
    type = 'news'
    nw = {
        'head': Head,
        'type': type
    }
    return render(request, 'testapp/index.html', nw)