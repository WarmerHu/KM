from django.shortcuts import  render_to_response
from django.template.context import RequestContext
#from showkm.k_means import kmeans
from kmeans import k_means

# Create your views here.

class K_C():
    k = []
    c = []
    def __init__(self, v):
        self.k = v['k']
        self.c = v['c']

def showkm(req):
    
    idLen, levelMax, s = k_means.kmeans()
    s = K_C(s[2])
    
    if req.POST.has_key('page'):
        p = req.GET['page']
        if p==1:
            s = K_C(s[0])
        elif p==10:
            s = K_C(s[1])
    
    return render_to_response('kmeans.html',
                              {'idLen':idLen, 'levelMax':levelMax, 's':s},
                              context_instance=RequestContext(req))