import requests
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import html
from django.views.decorators.csrf import csrf_exempt
from .cal_converter_trial import *
from .models import Greeting

# Create your views here.


def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")


def page2(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "page2.html")


def page3(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "page3.html")
# def index(request):
#    r = requests.get('http://httpbin.org/status/418')
#    print(r.text)
#    return HttpResponse('<pre>' + r.text + '</pre>')


def dumpdata(place, data):
    retval = ""
    if len(data) > 0:
        retval += '<p>Incoming '+place+' data:<br/>\n'
        for key, value in data.items():
            retval += html.escape(key) + '=' + html.escape(value) + '</br>\n'
        retval += '</p>\n'
    return retval

def form_trial(place, data):
    
    retval = ""
    if len(data) > 0:
        retval += '<p>Incoming '+place+' data:<br/>\n'
        retval += 'hello'
        for key, value in data.items():
            retval += html.escape(key) + '=' + str(html.escape(value)*2) + type(html.escape(value)) + '</br>\n'
            #retval += html.escape(key) + '=' + double_number(int(value)) + '</br>\n'
            #retval += str(double_number(html.escape(value)))
        retval += '</p>\n'
    return retval


@csrf_exempt
def html4(request):
    dump = dumpdata('POST', request.POST)
    return render(request, 'html4.html', {'data': dump})

# @csrf_exempt
def add_nums(request):
#    dump = dumpdata('POST', request.POST)
    return render(request, 'result.html')

@csrf_exempt
def chemda(request):
    val1 = int(request.POST.get('Month', False))
    val2 = int(request.POST.get('Day', False))
    val3 = int(request.POST.get('Year', False))
    res = eng_to_num(val1, val2, val3)
    res_2 = num_to_heb(res)
    #res = val1 + val2
    return render(request, 'chemda.html', {'data': res_2})


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})

def double_number(num):
    return int(num)*2

@csrf_exempt
def dateConvert(request):
    dump = dumpdata('POST', request.POST)
    return render(request, 'dateConvert.html', {'data': dump})
