from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import *
from django.contrib import messages
from .models import Vehicles
import csv,datetime,time

def upload(request):
    if request.method == 'POST':
        form = UploadCSV(request.POST,request.FILES)

        if form.is_valid():
            if 'vcsv' in request.FILES:
                csv_file=request.FILES['vcsv']
                db_obj=Vehicles()
                file_Reader =csv.reader(csv_file,delimiter=',')
                row=1
                for fields in file_Reader:
                    if row==1:
                        row=2
                        continue
                    db_obj.reg_num = str(fields[0])
                    db_obj.fuel_lvl = fields[3]
                    db_obj.ign_status = fields[2]
                    ts = datetime.datetime.now().timestamp()
                    print(ts)
                    db_obj.tmstmp=fields[4]
                    db_obj.lat=str(fields[1]).split("T")[0]
                    db_obj.lont=str(fields[1]).split("T")[1]
                    db_obj.save()

                #star = Loc.objects.filter(status='true')
                return HttpResponseRedirect('/upload')
        else:
            return HttpResponse("/upload")

    else:
        form = UploadCSV()
        db_obj=Vehicles.objects.all()
        print(db_obj)
        return render(request, 'Upload.html', {'form': form,'stp':db_obj})

def home(request):
    if request.method == 'POST':
        form = UploadCSV(request.POST,request.FILES)

        if form.is_valid():
            if 'vcsv' in request.FILES:
                csv_file=request.FILES['vcsv']
                if(csv_file.name.split(".")[1]!='csv'):
                    messages.error(request,"Only CSV")
                    return HttpResponseRedirect("/home")
                db_obj=Vehicles()
                file_Reader =csv.reader(csv_file,delimiter=',')
                row=1

                try:
                    for fields in file_Reader:
                        if row==1:
                            row=2
                            continue
                        db_obj.reg_num = str(fields[0])
                        db_obj.fuel_lvl = fields[3]
                        false_list=["FALSE","false","False","0"]
                        true_list=["TRUE","true","True","1"]

                        if fields[2] in false_list:
                            db_obj.ign_status =False

                        else:
                            db_obj.ign_status =True

                        db_obj.tmstmp=fields[4]
                        db_obj.lat=str(fields[1]).split("T")[0]
                        db_obj.lont=str(fields[1]).split("T")[1]
                        db_obj.save()

                    #star = Loc.objects.filter(status='true')
                    messages.success(request, "Uploaded successfully")
                    return HttpResponseRedirect('/home')
                except:
                    messages.error(request, "Invalid File Data")
                    return HttpResponseRedirect('/home')

        else:
            messages.error(request, "Invalid File")
            return HttpResponse("/home")

    else:
        form = UploadCSV()
        db_obj=Vehicles.objects.all()
        return render(request, 'Home.html', {'form': form,'stp':db_obj})

