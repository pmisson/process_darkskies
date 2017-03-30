# IPython log file

import json
import asciitable
import numpy as np
preguntas="darkskies_task_23_08_2014.json"
respuestas="darkskies_task_run_23_08_2014.json"
datos=open(respuestas, 'r').read()
resp=json.loads(datos)
datos1=open(preguntas, 'r').read()
pre=json.loads(datos1)
resp[0]
mias=[]
miclass=[]
        
for x in resp:
    if x['user_id']==3927:
        miclass.append(x['info']['classification'])
        mias.append(x['task_id'])
        
suyas=[]
suclass=[]
for x in resp:
    if x['user_id']==5305:
        suclass.append(x['info']['classification'])
        suyas.append(x['task_id'])
        
comunes=[]
for x in mias:
    try:
        comunes.append(suyas[suyas.index(x)])
    except:
        pass
    
  
clas_mia_comun=[]
clas_suya_comun=[]
for x in comunes:
    clas_mia_comun.append(miclass[mias.index(x)])
    clas_suya_comun.append(suclass[suyas.index(x)])
    
clas_suya_comun=np.array(clas_suya_comun)
clas_mia_comun=np.array(clas_mia_comun)
mask=clas_suya_comun==clas_mia_comun
mask
sum(mask)
len(comunes)

