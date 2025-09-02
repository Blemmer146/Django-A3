from django.shortcuts import render

# Create your views here.
def Names(request):
    """
    Render the names.html template with a list of names.
    """
    dic = {
        'fe': 'Arvind Sir',
        'be': 'Ravi Sir',
        'me': 'Prabhu Sir',
        'fa': 'Ajeet Sir',
    }
    return render(request, 'testapp/index.html', dic)
def Images(request):
    return render(request, 'testapp/photos.html')