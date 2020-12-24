from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from awgp.common.data import Recordset
from awgp.django.database import DB
from awgp.common.json import JSON
from awgp.common.response import Response
# Create your views here.
def indexView(request):
    # return HttpResponse("SHRAVAN")
    p = Post.objects.all()
    print(p)
    print(p[0].type.id)

    # r = Recordset()

    db = DB("default")
    r = db.runSelect("select id as code, tilte as title from itmgmt_post")
    # r.fromQueryset(p,{"title":"tilte","code":"id"})
    return render(request,"indexView.html",{"data":r.getJson()})


def updatView(request):
    data = request.POST.get("data")
    data = JSON.fromString(data)
    data = data[0]
    
    resp = Response()

    p = Post.objects.get(id=int(data["CODE"]))
    if p!=None:
        p.tilte = data["TITLE"]
        p.save()
        resp.success("Data save successfuly")
    else:
        resp.error("E001","Error in post retrive")


    return HttpResponse(resp.getJson())