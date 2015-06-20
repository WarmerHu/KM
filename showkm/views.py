from django.shortcuts import  render_to_response
from django.template.context import RequestContext
#from showkm.k_means import kmeans
from kmeans import k_means
from django.views.decorators.csrf import csrf_exempt
from django.http.response import HttpResponse, HttpResponseRedirect
from django.utils import simplejson
from django.core.paginator import Paginator, EmptyPage, InvalidPage

# Create your views here.



class K_C():
    k = []
    c = []
    def __init__(self, v):
        self.k = v['k']
        self.c = v['c']

def lastkm(req):
    return HttpResponseRedirect('/k_means/3')

@csrf_exempt
def showkm(req):
#    p = int(param.encode('utf8'))
    idMax,idMin, levelMax,levelMin, s = k_means.kmeans()
    paginator = Paginator([K_C(s[0]),K_C(s[1]),K_C(s[2]),K_C(s[3])],1)
    try:
        page = int(req.GET.get('page',3))
    except ValueError:
        page = 3
     
    print 'paginator:',paginator
    try:
        s = paginator.page(page)
    except (EmptyPage, InvalidPage):
        s = paginator.page(paginator.num_pages)   
    
    print 's:',s.object_list
    
    return render_to_response('kmeans.html',
                              {'idLen':idMax,'idMin':idMin, 'levelMax':levelMax,'levelMin':levelMin, 's':s},
                              context_instance=RequestContext(req))

@csrf_exempt
def kmAjax(req):
    if req.is_ajax():
        p = int((req.POST['page']).encode('utf8'))
        idMax,idMin, levelMax,levelMin, s = k_means.kmeans()
        a = simplejson.dumps({
             'idLen':idMax,'idMin':idMin, 'levelMax':levelMax,'levelMin':levelMin, 's':K_C(s[p])
             })
    return HttpResponse(a) 
