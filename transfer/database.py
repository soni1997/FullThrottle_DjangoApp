import simplejson
from .models import Employees
import json
from django.db import IntegrityError

# Create your views here.
# class Database for all database functions

class Database:
    # populate the database
    def populatedb():
        f = open("Test.json")
        data = json.load(f)
        for i in range(len(data["members"])):
            id = data["members"][i]["id"]
            name = data["members"][i]["real_name"]
            location = data["members"][i]["tz"]
            activity_per = data["members"][i]["activity_periods"]
            duration = ""
            for j in range(len(activity_per)):
                duration = duration + activity_per[j]["start_time"] + " to "+ activity_per[j]["end_time"] + ","
            try:
                Employees.objects.create(id = id, name = name, location = location, duration = duration)
            except IntegrityError:
                # ignores if we add the same id again(working on making it better)
                continue

    def conv_to_json():
        obj = Employees.objects.all()
        as_dict = []
        ok = 'true'
        for ob in obj:
            id = ob.id
            name = ob.name
            location = ob.location 
            duration = ob.duration
            duration = duration[0:len(duration)-1]
            duration = duration.split(',')
        
            activity_period = []
            for st in duration:
                st_end_index = st.find("to")
                start = st[0:st_end_index]
                end_start_index = st_end_index + 2
                end = st[end_start_index:len(st)]
                time = {
                    'start_time': start,
                    'end_time': end 
                }
                activity_period.append(time)
            temp = {
            'id':id,
            'name':name,
            'tz': location,
            'activity_period': activity_period
            }
            as_dict.append(temp)
        ev_as_dict = {
            'ok' : ok,
            'members': as_dict
        }
        simplejson.dumps(ev_as_dict)

        return ev_as_dict