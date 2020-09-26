from django.shortcuts import render
from django.http import HttpResponse

from .models import TEST
import json

class DATABASE:
    def populatedb():
        f = open('test.json')
        data = json.loads(f)

        for i in range(data["members"].len()):
            id = data["members"][i]["id"]
            name = data["members"][i]["real_name"]
            location = data["members"][i]["tz"]
            activity_per = data["members"][i]["activity_periods"]
            for j in range(activity_per.len()):
                start_time = activity_per[j]["start_time"]
                end_time = activity_per[j]["end_time"]
                Test.objects.create(id = id, name = name, location = location, start_time = start_time, end_time = end_time)