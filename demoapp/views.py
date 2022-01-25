from django.shortcuts import redirect, render
from demoapp.models import VehicleDetail
from demoapp.models import VehicleType,EngineStatus
# Create your views here.
from django.core.files.storage import FileSystemStorage

def Createdata(request):
    if request.method=="GET":
        data=VehicleDetail.objects.all()
        data1=VehicleType
        data2=EngineStatus
        return render(request, 'create.html', locals())
    else:
        vtype = request.POST.get("vtype")
        vnumber = request.POST.get("vnumber")
        vstatus = request.POST.get("vstatus")
        vspeed = request.POST.get("vspeed")
        vaveragespeed = request.POST.get("vaveragespeed")
        vtemperature = request.POST.get("vtemperature")
        vfuellevel = request.POST.get("vfuellevel")
        venginestatus = request.POST.get("venginestatus")
        
        statusv=""
        if vstatus=="on":
            statusv="True"
        else: statusv="False"
        
            
        ab = VehicleDetail.objects.create(
            Type=vtype,
            Number=vnumber,
            Status=statusv,
            Speed=vspeed,
            Averagespeed=vaveragespeed,
            Temperature=vtemperature,
            Fuellevel=vfuellevel,
            Enginestatus=venginestatus,
        )
        data=VehicleDetail.objects.all()
        data1=VehicleType
        
        return render(request, 'create.html', locals())

def Datalist(request):
    data=VehicleDetail.objects.all()
    return render(request,"list.html",locals())
def Datadetail(request,vid):
    if request.method=="GET":
        data=VehicleDetail.objects.get(id=vid)
        return render(request,'detail.html',locals())
    else:
        data=VehicleDetail.objects.get(id=vid)
        status1=request.POST.get("offstatus")
        status2=request.POST.get("onstatus")
        print(status1)
        print(status2)
        statusv=""
        if status1=="off":
            statusv="False"
        if status2=="on":
            statusv="True"
        data.Status=statusv
        data.save()
        data=VehicleDetail.objects.get(id=vid)
        return render(request,'detail.html',locals())
def Dataupdate(request,vid):
    if request.method=="GET":
        data=VehicleDetail.objects.get(id=vid)
        data1=VehicleType
        data2=EngineStatus
        return render(request, 'update.html', locals())
    else:
        data=VehicleDetail.objects.get(id=vid)
        data.Type = request.POST.get("vtype")
        data.Number = request.POST.get("vnumber")
        data.Speed = request.POST.get("vspeed")
        data.Averagespeed = request.POST.get("vaveragespeed")
        data.Temperature = request.POST.get("vtemperature")
        data.Fuellevel = request.POST.get("vfuellevel")

        vstatus = request.POST.get("vstatus")
        venginestatus = request.POST.get("venginestatus")
        statusv=""
        
        if vstatus=="on":
            statusv="True"
        else: statusv="False"
        
        data.Status = statusv
        data.Enginestatus = venginestatus
        data.save()
        data=VehicleDetail.objects.get(id=vid)
        data1=VehicleType
        data2=EngineStatus
        
        return render(request, 'update.html', locals())
def Aboutpage(request):
    return render(request,'about.html',locals())

def Datadelete(request,vid):
    data=VehicleDetail.objects.get(id=vid)
    data.delete()
    return redirect("list.html")