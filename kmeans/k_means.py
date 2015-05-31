#coding:utf-8
'''
Created on 2015-5-25
@author: 3213006173-胡楚晴
description:k-means
'''
from django.db.models.aggregates import Max, Min
from kmeans.models import Movie
import random
def readModel():
#    sql1 = 'SELECT _id, _comment_level FROM movie'
#    sql2 = 'SELECT COUNT() FROM Movie'
#    sql3 = 'SELECT MAX(_comment_level) FROM Movie'
#    sql1 = movie.objects.raw(sql1)
    sql1 = list(Movie.objects.all().values('field_id','field_comment_level'))
    sql2 = Movie.objects.aggregate(Max('field_id'))
    sql22 = Movie.objects.aggregate(Min('field_id'))
    sql3 = Movie.objects.aggregate(Max('field_comment_level'))
    sql33 = Movie.objects.aggregate(Min('field_comment_level'))
    sql4 = Movie.objects.count()
    
        
    return sql1, sql2['field_id__max'], sql22['field_id__min'], sql3['field_comment_level__max'],sql33['field_comment_level__min'], sql4
    
    
def distance(v,k):
    return abs(v[0]-k[0])**2 + abs(v[1]-k[1])**2

def min(v1,v2,v3):
    i = 3
    if v1 < v2:
        v1,v2 = v2, v1
        i = 1
    if v2 < v3:
        v2,v3 = v3,v2
        if i!=1:
            i = 2
    return i

def avg(v,k):
    if not v:
        return k
    x = 0
    y = 0
    for i in v:
        x += i[0]
        y += i[1]
    return [x/len(v), y/len(v), k[2]]
        
def kmeans():
    D,idMax,idMin,levelMax,levelMin,num = readModel() 
    
    for i,p in enumerate(D):
#        if type(p)==dict:
#            p = [D[i]['field_id'],D[i]['field_comment_level']]
        D[i]=[D[i]['field_id'],D[i]['field_comment_level'],1]
    
    k11 = D[random.randint(0,num)]
    C1 = []
    while(True):
        i  =  random.randint(0,num-1)
        if D[i]!=k11:
            break
    k22 = [D[i][0],D[i][1],2]
    C2 = []
    while(True):
        i  =  random.randint(0,num)
        if D[i]!=k11 and D[i]!=k22:
            break
    k33 = [D[i][0],D[i][1],3]
    C3 = []
    t = 0
    s = []   
    
    for p in D:
        i = min(distance(p,k11),distance(p,k22),distance(p,k33))
        if i==1:
            C1.append([p[0],p[1],1])
        elif i==2:
            C2.append([p[0],p[1],2])
        else:
            C3.append([p[0],p[1],3])
    k = []
    k.append(k11)
    k.append(k22)
    k.append(k33)
    c = C1 + C2 + C3
    s.append({'k':k,'c':c})
    k1 = k11
    k11 = avg(C1,k1)
    k2 = k22
    k22 = avg(C2,k2)
    k3 = k33
    k33 = avg(C3,k3)
    num = []
    
    while k1!=k11 or k2!=k22 or k3!=k33:
        t += 1
        
        for j,p in enumerate(C1):
            i = min(distance(C1[j],k11),distance(C1[j],k22),distance(C1[j],k33))
            if i==2:
                C2.append([C1[j][0],C1[j][1],2])
                num.append(p)
            elif i==3:
                C3.append([C1[j][0],C1[j][1],3])
                num.append(p)
        for j in num:
            C1.remove(j)
        num = []
        for j,p in enumerate(C2):
            i = min(distance(p,k11),distance(p,k22),distance(p,k33))
            if i==1:
                C1.append([p[0],p[1],1])
                num.append(p)
            elif i==3:
                C3.append([p[0],p[1],3])
                num.append(p)
        for j in num:
            C2.remove(j)
        num = []
        for j,p in enumerate(C3):
            i = min(distance(p,k11),distance(p,k22),distance(p,k33))
            if i==1:
                C1.append([p[0],p[1],1])
                num.append(p)
            elif i==2:
                C2.append([p[0],p[1],2])
                num.append(p)
        for j in num:
            C3.remove(j)
        num = []
        if t==1 or t==2:
            k = []
            k.append(k11)
            k.append(k22)
            k.append(k33)
            c = C1 + C2 + C3
            s.append({'k':k,'c':c})

        k1 = k11
        k11 = avg(C1,k1)
        k2 = k22
        k22 = avg(C2,k2)
        k3 = k33
        k33 = avg(C3,k3)
        
    s.append({'k':k,'c':c})
    return idMax,idMin, int(levelMax)+1,levelMin, s 