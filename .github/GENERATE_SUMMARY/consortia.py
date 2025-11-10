import cmipld
import os
from cmipld.utils.ldparse import *
from cmipld.utils.checksum import version

me = __file__.split('/')[-1].replace('.py','')

def run(whoami, path, name, url, io):
    
    
    
    url = f'{whoami}:organisation/graph.jsonld'
    
    data = cmipld.get(url,depth=1)['@graph']
    
    summary = name_extract(data,['validation-key','ui_label','url','members'])
    
    
    for i in summary:
        summary[i] = set(summary[i].get('members', dict()).keys())
    
    location = f'{path}/{name.lower()}_{me}.json'
    return location, me, summary