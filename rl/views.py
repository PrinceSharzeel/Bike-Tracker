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
                    messages.error(request,"Only CSV files allowed")
                    return HttpResponseRedirect("/home")
                decoded_file = csv_file.read().decode('utf-8').splitlines()
                file_reader = csv.DictReader(decoded_file)
                for fields in file_reader:
                    #fields = str(entry[0]).split(',')
                    reg_num=str(fields[0]).upper()
                    ign_status = fields[2]
                    fuel_lvl = fields[3]
                    lat = str(fields[1]).split("T")[0]
                    lont = str(fields[1]).split("T")[1]
                    tmstmp = fields[4]
                    if validate_vehicle(reg_num)==False:
                        messages.error(request, "Invalid Vehicle Number")
                        return HttpResponseRedirect("/home")


                    db_obj = Vehicles()
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
                    print(db_obj)
                    db_obj.save()

                messages.success(request, "Uploaded successfully")
                return HttpResponseRedirect('/home')

        else:
            messages.error(request, "Invalid File")
            return HttpResponse("/home")

    else:
        form = UploadCSV()
        db_obj=Vehicles.objects.all()
        return render(request, 'Home.html', {'form': form,'stp':db_obj})



def validate_vehicle(reg_num):
    pattern = '^[A-Z]{2}[0-9]{2}[A-Z]{2}[0-9]{4}$'
    result = re.match(pattern, reg_num)

    print(result)
    if result:
       return True

    return False



