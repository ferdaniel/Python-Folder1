from django.shortcuts import render
from django.http import HttpResponse
import urllib2
# Create your views here.

def home(request):
    try:
	f= urllib2.urlopen("http://mejorando.la")
	g= f.read()
	f.close()
    except HTTPError, e:
	print "Error!!"
	print e.code
    
    except HTTPError, e:
	print "Error!!"
	print e.code	

    return HttpResponse(g)

def home2(request):
    return HttpResponse("home 2 mdf")

def post(request,id_post):
    if int(id_post)> 10 :	
        return HttpResponse("Este post es mayor que 10: %s" % id_post)
    else:
	return HttpResponse("Este post es menor que 10: %s" % id_post)

def live(request,id1,id2):
    return HttpResponse("Este es el post %s y %s" % (id1,id2))

def request(request):
    return HttpResponse("Consulta %s" % request)



