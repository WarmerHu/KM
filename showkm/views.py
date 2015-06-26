from django.shortcuts import  render_to_response
from django.template.context import RequestContext
#from showkm.k_means import kmeans
from kmeans import k_means
from django.views.decorators.csrf import csrf_exempt
from django.http.response import  HttpResponseRedirect

# Create your views here.


#创建用于展现的数据结构
class K_C():
    k = []
    c = []
    def __init__(self, v):
        self.k = v['k']
        self.c = v['c']

#主页重定向
def lastkm(req):
    return HttpResponseRedirect('/km/3')




def kmshow(req,param):
#    格式化获得的参数
    p = int(param.encode('utf8'))
#    获取相应数据
    idMax,idMin, levelMax,levelMin, s = k_means.kmeans()
#    paginator = Paginator([K_C(s[0]),K_C(s[1]),K_C(s[2]),K_C(s[3])],1)
#    try:
#        page = int(req.GET.get('page',4))
#    except ValueError:
#        page = 4
#     
#    try:
#        s = paginator.page(page)
#    except (EmptyPage, InvalidPage):
#        s = paginator.page(paginator.num_pages)   
#
#    for i,p in enumerate(s):    
#        s[i] = K_C(p)
    

    return render_to_response('kmeans.html',
                              {'idLen':idMax,'idMin':idMin, 'levelMax':levelMax,'levelMin':levelMin, 's':K_C(s[p])},
                              context_instance=RequestContext(req))


