from django.shortcuts import  render_to_response
from django.template.context import RequestContext
#from showkm.k_means import kmeans
from kmeans import k_means
from django.views.decorators.csrf import csrf_exempt
from django.http.response import HttpResponse
import json
from django.utils import simplejson

# Create your views here.

class K_C():
    k = []
    c = []
    def __init__(self, v):
        self.k = v['k']
        self.c = v['c']

@csrf_exempt
def showkm(req):
    
    idMax,idMin, levelMax,levelMin, s = k_means.kmeans()
    p = 3
    if req.is_ajax():
        p = int((req.POST['page']).encode('utf8'))
    
    return render_to_response('kmeans.html',
                              {'idLen':idMax,'idMin':idMin, 'levelMax':levelMax,'levelMin':levelMin, 's':K_C(s[p])},
                              context_instance=RequestContext(req))

@csrf_exempt
def kmAjax(req):
    if req.is_ajax():
        p = int((req.POST['page']).encode('utf8'))
        idMax,idMin, levelMax,levelMin, s = k_means.kmeans()
        a = simplejson.dumps({
             'idLen':idMax,'idMin':idMin, 'levelMax':levelMax,'levelMin':levelMin, 's':K_C(s[p])
             })
    return HttpResponse() 
