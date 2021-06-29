import json
import math
# Add the functions in this file
def load_journal(file_name):
    with open(file_name,'r') as f:
        return json.load(f)

def compute_phi(file_name,event):
    a=0
    b=0
    c=0
    d=0
    e=0
    f=0
    g=0
    h=0
    with open(file_name,'r') as f:
        data=json.load(f)
        for datum in data:
            if (event in datum['events']) and (datum['squirrel']=='False'):
                a+=1
            if (event not in datum['events']) and (datum['squirrel']!='False'):
                b+=1
            if (event in datum['events']) and (datum['squirrel']!='False'):
                c+=1
            if (event not in datum['events']) and (datum['squirrel']=='False'):
                d+=1
            if (event in datum['events']):
                e+=1
            if (event not in datum['events']):
                f+=1
            if (datum['squirrel']=='False'):
                g+=1
            if (datum['squirrel']!='False'):
                h+=1
    return (a*b-c*d)/math.sqrt(e*f*g*h)

def compute_correlations(file_name):
    data=load_journal(file_name)
    events_list=[]
    for datum in data:
        for event in datum['events']:
            if event not in events_list:
                events_list.append(event)
    ret={}
    for event in events_list:
        ret[event]=compute_phi(file_name,event)
    return ret

def diagnose(file_name):
    corrs=compute_correlations(file_name)
    hp_val=hn_val=0
    for key,value in corrs.items():
        if value>=hp_val:
            hp_val=value
            hp_key=key
        if value<=hn_val:
            hn_val=value
            hn_key=key
    return hp_key,hn_key
