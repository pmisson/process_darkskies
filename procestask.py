# IPython log file

import json
import asciitable
import numpy as np
preguntas="darkskies_task_22_08_2014.json"
respuestas="darkskies_task_run_22_08_2014.json"
datos=open(respuestas, 'r').read()
resp=json.loads(datos)
datos1=open(preguntas, 'r').read()
pre=json.loads(datos1)
def get_cloudy(g):
    k=[]
    for x in g:
     if x['info']['cloudy']=='cloudy':
         k.append(0)
     elif x['info']['cloudy']=='someclouds':
         k.append(1)
     elif x['info']['cloudy']=='clear':
         k.append(2)
     elif x['info']['cloudy']=='':
         #k.append(-1)
         pass
    
    gmean=np.mean(k)
    gmedian=np.median(k)
    return gmean,gmedian,k
     
def get_sharp(g):
    k=[]
    for x in g:
     try:
         if x['info']['sharp']=='sharp':
             k.append(1)
         elif x['info']['sharp']=='blurry':
             k.append(0)
         elif x['info']['sharp']=='':
            pass
     except:
        print 'fallo'
    
    gmean=np.mean(k)
    gmedian=np.median(k)
    return gmean,gmedian,k
    
    
def get_class(g):
    k=[]
    for x in g:
     if x['info']['classification']=='city':
         k.append(0)
     elif x['info']['classification']=='stars':
         k.append(1)
     elif x['info']['classification']=='black':
         k.append(-1)
     elif x['info']['classification']=='aurora':
         k.append(-3)
     elif x['info']['classification']=='astronaut':
         k.append(-6)
     elif x['info']['classification']=='None':
         k.append(-19)
     elif x['info']['classification']=='404':
         k.append(-20)
     elif x['info']['classification']=='unknown':
         k.append(-21)         
         
    
    gmean=np.mean(k)
    gmedian=np.median(k)
    return gmean,gmedian,k

ID=[]
ID_NASA=[]     
for x in range(len(pre)):
         ID.append(pre[x]['id'])
         ID_NASA.append(pre[x]['info']['idiss'])
         

resp_clas=range(len(pre))
clas_all=range(len(pre))    
sharp_all=range(len(pre))    
cloudy_all=range(len(pre))
clas_mean=range(len(pre))    
sharp_mean=range(len(pre))    
cloudy_mean=range(len(pre))
clas_med=range(len(pre))    
sharp_med=range(len(pre))    
cloudy_med=range(len(pre))

clas_med3=range(len(pre))
clas_med5=range(len(pre))
clas_med10=range(len(pre))
clas_med15=range(len(pre))
clas_med20=range(len(pre))
clas_med25=range(len(pre))

sharp_med3=range(len(pre))
sharp_med5=range(len(pre))
sharp_mean5=range(len(pre))
sharp_med10=range(len(pre))
sharp_med15=range(len(pre))
sharp_med20=range(len(pre))
sharp_med25=range(len(pre))

cloudy_med3=range(len(pre))
cloudy_med5=range(len(pre))
cloudy_mean5=range(len(pre))
cloudy_med10=range(len(pre))
cloudy_med15=range(len(pre))
cloudy_med20=range(len(pre))
cloudy_med25=range(len(pre))

lenclas=range(len(pre))
lencloudy=range(len(pre))
lensharp=range(len(pre))
  
for x in range(len(pre)):
    resp_clas[x]=[]
       
for x in range(len(resp)):
    id=ID.index(resp[x]['task_id'])
    resp_clas[id].append(resp[x])
    
for x in range(len(resp_clas)):
    (clas_mean[x],clas_med[x],clas_all[x])=get_class(resp_clas[x])
    (cloudy_mean[x],cloudy_med[x],cloudy_all[x])=get_cloudy(resp_clas[x])
    (sharp_mean[x],sharp_med[x],sharp_all[x])=get_sharp(resp_clas[x])
    lenclas[x]=len(clas_all[x])
    lencloudy[x]=len(cloudy_all[x])
    lensharp[x]=len(sharp_all[x])

lenclas=np.array(lenclas)
lencloudy=np.array(lencloudy)
lensharp=np.array(lensharp)
lenclas5=lenclas>10
lenclas10=lenclas>10
lenclas15=lenclas>15
lenclas20=lenclas>20
lenclas25=lenclas>25
lenclas29=lenclas>29

lencloudy5=lencloudy>5
lencloudy10=lencloudy>10
lencloudy15=lencloudy>15
lencloudy20=lencloudy>20
lencloudy25=lencloudy>25
lencloudy29=lencloudy>29

lensharp5=lensharp>10
lensharp10=lensharp>10
lensharp15=lensharp>15
lensharp20=lensharp>20
lensharp25=lensharp>25
lensharp29=lensharp>29

for x in range(len(resp_clas)):

    clas_med3[x]=np.median(clas_all[x][:3])    
    clas_med5[x]=np.median(clas_all[x][:5])
    clas_med10[x]=np.median(clas_all[x][:10])
    clas_med15[x]=np.median(clas_all[x][:15])
    clas_med20[x]=np.median(clas_all[x][:20])
    clas_med25[x]=np.median(clas_all[x][:25])
    cloudy_med3[x]=np.median(cloudy_all[x][:3])
    cloudy_mean5[x]=np.mean(cloudy_all[x][:25])#5
    cloudy_med5[x]=np.median(cloudy_all[x][:5])
    cloudy_med10[x]=np.median(cloudy_all[x][:10])
    cloudy_med15[x]=np.median(cloudy_all[x][:15])
    cloudy_med20[x]=np.median(cloudy_all[x][:20])
    cloudy_med25[x]=np.median(cloudy_all[x][:25])
    sharp_med3[x]=np.median(sharp_all[x][:3])
    sharp_med5[x]=np.median(sharp_all[x][:5])
    sharp_mean5[x]=np.mean(sharp_all[x][:25])#5
    sharp_med10[x]=np.median(sharp_all[x][:10])
    sharp_med15[x]=np.median(sharp_all[x][:15])
    sharp_med20[x]=np.median(sharp_all[x][:20])
    sharp_med25[x]=np.median(sharp_all[x][:25])

clas_dif3=np.array(clas_med3)[lenclas5]-np.array(clas_med)[lenclas5]
clas_dif5=np.array(clas_med5)[lenclas10]-np.array(clas_med)[lenclas10]
clas_dif10=np.array(clas_med10)[lenclas15]-np.array(clas_med)[lenclas15]
clas_dif15=np.array(clas_med15)[lenclas20]-np.array(clas_med)[lenclas20]
clas_dif20=np.array(clas_med20)[lenclas25]-np.array(clas_med)[lenclas25]    
clas_dif25=np.array(clas_med25)[lenclas29]-np.array(clas_med)[lenclas29]

dif_clas3=float(sum(clas_dif3!=0))/sum(clas_dif3==0)*100
dif_clas5=float(sum(clas_dif5!=0))/sum(clas_dif5==0)*100
dif_clas10=float(sum(clas_dif10!=0))/sum(clas_dif10==0)*100
dif_clas15=float(sum(clas_dif15!=0))/sum(clas_dif15==0)*100
dif_clas20=float(sum(clas_dif20!=0))/sum(clas_dif20==0)*100
dif_clas25=float(sum(clas_dif25!=0))/sum(clas_dif25==0)*100

dif2_clas3=float(sum(clas_dif3!=0))/len(clas_dif3)*100
dif2_clas5=float(sum(clas_dif5!=0))/len(clas_dif5)*100
dif2_clas10=float(sum(clas_dif10!=0))/len(clas_dif10)*100
dif2_clas15=float(sum(clas_dif15!=0))/len(clas_dif15)*100
dif2_clas20=float(sum(clas_dif20!=0))/len(clas_dif20)*100
dif2_clas25=float(sum(clas_dif25!=0))/len(clas_dif25)*100

cloudy_dif3=np.array(cloudy_med3)[lencloudy5]-np.array(cloudy_med)[lencloudy5]
cloudy_dif5=np.array(cloudy_med5)[lencloudy10]-np.array(cloudy_med)[lencloudy10]
cloudy_dif10=np.array(cloudy_med10)[lencloudy15]-np.array(cloudy_med)[lencloudy15]
cloudy_dif15=np.array(cloudy_med15)[lencloudy20]-np.array(cloudy_med)[lencloudy20]
cloudy_dif20=np.array(cloudy_med20)[lencloudy25]-np.array(cloudy_med)[lencloudy25]    
cloudy_dif25=np.array(cloudy_med25)[lencloudy29]-np.array(cloudy_med)[lencloudy29]

dif_cloudy3=float(sum(cloudy_dif3!=0))/sum(cloudy_dif3==0)*100
dif_cloudy5=float(sum(cloudy_dif5!=0))/sum(cloudy_dif5==0)*100
dif_cloudy10=float(sum(cloudy_dif10!=0))/sum(cloudy_dif10==0)*100
dif_cloudy15=float(sum(cloudy_dif15!=0))/sum(cloudy_dif15==0)*100
dif_cloudy20=float(sum(cloudy_dif20!=0))/sum(cloudy_dif20==0)*100
dif_cloudy25=float(sum(cloudy_dif25!=0))/sum(cloudy_dif25==0)*100

sharp_dif3=np.array(sharp_med3)[lensharp5]-np.array(sharp_med)[lensharp5]
sharp_dif5=np.array(sharp_med5)[lensharp10]-np.array(sharp_med)[lensharp10]
sharp_dif10=np.array(sharp_med10)[lensharp15]-np.array(sharp_med)[lensharp15]
sharp_dif15=np.array(sharp_med15)[lensharp20]-np.array(sharp_med)[lensharp20]
sharp_dif20=np.array(sharp_med20)[lensharp25]-np.array(sharp_med)[lensharp25]    
sharp_dif25=np.array(sharp_med25)[lensharp29]-np.array(sharp_med)[lensharp29]

dif_sharp3=float(sum(sharp_dif3!=0))/sum(sharp_dif3==0)*100
dif_sharp5=float(sum(sharp_dif5!=0))/sum(sharp_dif5==0)*100
dif_sharp10=float(sum(sharp_dif10!=0))/sum(sharp_dif10==0)*100
dif_sharp15=float(sum(sharp_dif15!=0))/sum(sharp_dif15==0)*100
dif_sharp20=float(sum(sharp_dif20!=0))/sum(sharp_dif20==0)*100
dif_sharp25=float(sum(sharp_dif25!=0))/sum(sharp_dif25==0)*100

mask_stars=np.array(clas_med25)==1
mask_city=np.array(clas_med25)==0
mask_black=np.array(clas_med25)==-1
mask_aurora=np.array(clas_med25)==-3
mask_astronaut=np.array(clas_med25)==-6
mask_None=np.array(clas_med25)==-19
mask_404=np.array(clas_med25)==-20
mask_unknown=np.array(clas_med25)==-21

fewclouds=np.array(cloudy_mean5)>0.7
sharpmask=np.array(sharp_mean5)>0.3



stars=np.array(ID_NASA)[mask_stars]
stars=list(stars)
f = open('stars.txt', 'w')
f.write("\n".join(stars))
f.close()

maskS1=mask_stars*fewclouds*sharpmask

stars=np.array(ID_NASA)[maskS1]
stars=list(stars)
f = open('stars1.txt', 'w')
f.write("\n".join(stars))
f.close()

aurora=np.array(ID_NASA)[mask_aurora]
aurora=list(aurora)
f = open('aurora.txt', 'w')
f.write("\n".join(aurora))
f.close()

city=np.array(ID_NASA)[mask_city]
city=list(city)
f = open('city.txt', 'w')
f.write("\n".join(city))
f.close()

maskC1=mask_city*fewclouds*sharpmask

city1=np.array(ID_NASA)[maskC1]
city1=list(city1)
f = open('city1.txt', 'w')
f.write("\n".join(city1))
f.close()


black=np.array(ID_NASA)[mask_black]
black=list(black)
f = open('black.txt', 'w')
f.write("\n".join(black))
f.close()

astronaut=np.array(ID_NASA)[mask_astronaut]
astronaut=list(astronaut)
f = open('astronaut.txt', 'w')
f.write("\n".join(astronaut))
f.close()

none=np.array(ID_NASA)[mask_None]
none=list(none)
f = open('none.txt', 'w')
f.write("\n".join(none))
f.close()

n404=np.array(ID_NASA)[mask_404]
n404=list(n404)
f = open('404.txt', 'w')
f.write("\n".join(n404))
f.close()

unknown=np.array(ID_NASA)[mask_unknown]
unknown=list(unknown)
f = open('unknown.txt', 'w')
f.write("\n".join(unknown))
f.close()
