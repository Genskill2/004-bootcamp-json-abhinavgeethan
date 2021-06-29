import json
import math
# Add the functions in this file
def load_journal(file_name):
    with open(file_name,'r') as f:
        return json.load(f)

def compute_phi(file_name,event):
    n11=n00=n10=n01=n13=n03=n31=n30=0
    with open(file_name,'r') as f:
        data=json.load(f)
        for datum in data:
            if (event in datum['events']) and (datum['squirrel']=='False'):
                n11+=1
            if (event not in datum['events']) and (datum['squirrel']!='False'):
                n00+=1
            if (event in datum['events']) and (datum['squirrel']!='False'):
                n10+=1
            if (event not in datum['events']) and (datum['squirrel']=='False'):
                n01+=1
            if (event in datum['events']):
                n13+=1
            if (event not in datum['events']):
                n03+=1
            if (datum['squirrel']=='False'):
                n31+=1
            if (datum['squirrel']!='False'):
                n30+=1
    return (n11*n00-n10*n01)/math.sqrt(n13*n03*n31*n30)

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
