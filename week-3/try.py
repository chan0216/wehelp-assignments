import urllib.request as request
import json
import csv
scr="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with request.urlopen(scr) as response:
    data=json.load(response)
    slist=data["result"]["results"]
    clist=[]
with open("data.csv","w",encoding="utf-8",newline="") as f: 
    w = csv.writer(f)
    for n in slist:
        list=n["file"].split("http")[1]
        olist="http"+list
        list1=n["stitle"],n["address"][5:8],n["longitude"],n["latitude"],olist
        clist.append(list1)
    w.writerows(clist)