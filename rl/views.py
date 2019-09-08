from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import *
from django.contrib import messages
from .models import Vehicles
import csv,datetime,time,re

def Vehicle_Map(request):
    db_obj = Vehicles.objects.all()
    print(db_obj)
    return render(request, 'Map.html', {'vehicles_lst': db_obj})




def home(request):
    if request.method == 'POST':
        form = UploadCSV(request.POST,request.FILES)

        if form.is_valid():
            if 'vcsv' in request.FILES:
                csv_file=request.FILES['vcsv']
                if csv_file.name.split(".")[1]!='csv':
                    messages.error(request,"Only CSV")
                    return HttpResponseRedirect("/home")
                db_obj=Vehicles()
                file_reader =csv.reader(csv_file,delimiter=',')
                row=1

                try:
                    for fields in file_reader:
                        if row==1:
                            row=2
                            continue
                        reg_num=fields[0]
                        ign_status = fields[2]
                        fuel_lvl = fields[3]
                        lat = str(fields[1]).split("T")[1]
                        lont = str(fields[1]).split("T")[1]
                        tmstmp = fields[4]

                        db_obj.reg_num = reg_num
                        db_obj.fuel_lvl = fuel_lvl

                        false_list = ["FALSE","false","False","0"]

                        if ign_status in false_list:
                            db_obj.ign_status =False

                        else:
                            db_obj.ign_status =True

                        db_obj.tmstmp=tmstmp
                        db_obj.lat=lat
                        db_obj.lont=lont
                        db_obj.save()

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



def validate_entries(reg_num,lat,lont):

    reg_pattern = re.compile('^[A-Z]{2}[ -][0-9]{1,2}(?: [A-Z])?(?: [A-Z]*)? [0-9]{4}$')

    lattitude_patrn = re.compile("^(\\+|-)?(?:90(?:(?:\\.0{1,6})?)|(?:[0-9]|[1-8][0-9])(?:(?:\\.[0-9]{1,6})?))$")
    longitude_patrn = re.compile("^(\\+|-)?(?:180(?:(?:\\.0{1,6})?)|(?:[0-9]|[1-9][0-9]|1[0-7][0-9])(?:(?:\\.[0-9]{1,6})?))$")

    if reg_pattern.match(reg_num)==False:
        print("reg_failed")
        return False
    if lattitude_patrn.match(lat)==False:
        print("lat_failed")
        return False
    if longitude_patrn.match(lont)==False:
        print("lon_failed")
        return False

    return True



