import json
import math
# Add the functions in this file
def load_journal(file_name):
    with open(file_name,'r') as f:
        return json.load(f)

def compute_phi(file_name,event):
    a=1
    b=1
    c=1
    d=1
    e=1
    f=1
    g=1
    h=1
    ctr=0
    with open(file_name,'r') as file:
        data=json.load(file)
        for datum in data:
            if (event in datum['events']) and (datum['squirrel']=='False'):
                if not ctr==0:
                    a+=1
            if (event not in datum['events']) and (datum['squirrel']!='False'):
                if not ctr==0:
                    b+=1
            if (event in datum['events']) and (datum['squirrel']!='False'):
                if not ctr==0:
                    c+=1
            if (event not in datum['events']) and (datum['squirrel']=='False'):
                if not ctr==0:
                    d+=1
            if (event in datum['events']):
                if not ctr==0:
                    e+=1
            if (event not in datum['events']):
                if not ctr==0:
                    f+=1
            if (datum['squirrel']=='False'):
                if not ctr==0:
                    g+=1
            if (datum['squirrel']!='False'):
                if not ctr==0:
                    h+=1
            ctr+=1
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
