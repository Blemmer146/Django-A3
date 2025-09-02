import datetime

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def display(request):
    current=datetime.datetime.now()
    date = current.strftime('%d/%m/%Y')
    hour=int(current.strftime('%H'))
    st=f'<h1>INSURANCE PORTAL '
    # st='<h1> Good Afternoon the date today is '+str(date)+'</h1>'
    if 12<hour<16:
        st=st.replace('Morning','Afternoon')
    elif hour<20:
        st=st.replace('Morning', 'Evening')
    elif hour>20:
        st = st.replace('Morning', 'Night')
    st+='</h1><hr>'
    st+=f'<h3>Good Morning the date today is {date} and hour is {hour}</h3><br>'
    st+=f'<ol><h2><li><a href=http://127.0.0.1:7777/call/hom/> Home Insurance </a></li></h2><br>'
    st+=f'<h2><li><a href=http://127.0.0.1:7777/call/lif/> Life Insurance </a></li></h2><br>'
    st+=f'<h2><li><a href=http://127.0.0.1:7777/call/car/> Car Insurance </a></li></h2><br></ol>'

    return HttpResponse(st)


def homins(request):
    st='Home Insurance'
    return HttpResponse(st)
def lifins(request):
    st='Life Insurance'
    return HttpResponse(st)
def carins(request):
    st='Car Insurance'
    return HttpResponse(st)
