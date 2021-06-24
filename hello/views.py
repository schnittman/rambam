import requests
from django.shortcuts import render
from django.http import HttpResponse

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
#def index(request):
#    r = requests.get('http://httpbin.org/status/418')
#    print(r.text)
#    return HttpResponse('<pre>' + r.text + '</pre>')

@csrf_exempt
def html4(request):
    dump = dumpdata('POST', request.POST)
    return render(request, 'getpost/html4.html', {'data' : dump })

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
