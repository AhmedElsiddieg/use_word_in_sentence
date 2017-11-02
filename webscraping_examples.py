# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 13:47:49 2017

@author: ahmed
"""
import sys
import bs4 as bs
import urllib2 
import urllib
from urllib2 import urlopen

#chganging output to file 
f= open("beyondHitParade2.txt",'w')
sys.stdout=f

#wordsHitParade4='acerbic,aggrandize,alchemy,amenable,anachronism,astringent,contiguous,convention,credulous,cynicism,decorum,derision,desiccate,dilettante,disparage,divulge,fawn,flout,garrulous,glib,hubris,imminent,immutable,impetuous,indifferent,inimical,intractable,intrepid,laconic,maverick,mercurial,mollify,neophyte,obfuscate,obstinate,ostentatious,pervade,phlegmatic,plethora,pragmatic,presumption,pristine,probity,proclivity,proliferate,propensity,prosaic,pungent,quixotic,quotidian,rarefy,recondite,refulgent,renege,sedulous,shard,soporific,sparse,spendthrift,subtle,tacit,terse,tout,trenchant,unfeigned,untenable,vacillate,variegated,vexation,vigilant,vituperate,volatile'
#wordsBeyondHitParade1='alloy,appropriate,arrest,august,bent,broach,brook,cardinal,chauvinist,color,consequential,damp,die,essay,exact,fell,flag,flip,ford,grouse,guy,intimate,list,lumber,meet,milk,mince,nice,occult,pedestrian,pied,pine,plastic,pluck,prize,rail,rent,quail,qualify,sap,scurvy,singular,stand,steep,strut,table,tender,waffle,wag'
words='abjure,adumbrate,anathema,anodyne,apogee,apostate,apotheosis,asperity,asseverate,assiduous,augury,bellicose,calumniate,captious,cavil,celerity,chimera,contumacious,debacle,denouement,descry,desuetude,desultory,diaphanous,diffident,dirge,encomium,eschew,excoriate,execrate,exegesis,expiate,extirpate,fatuous,fractious,gainsay,heterodox,imbroglio,indefatigable,ineluctable,inimitable,insouciant,inveterate,jejune,lubricious,mendicant,meretricious,minatory,nadir,nonplussed,obstreperous,ossified,palliate,panegyric,parsimonious,pellucid,peroration,plangent,prolix,propitiate,puerile,puissance,pusillanimous,remonstrate,sagacious,salacious,salutary,sanguine,saturnine,sententious,stentorian,stygian,sycophant,tendentious,timorous,tyro,vitiate,voluble'
wordList=words.split(",")
#changing the user-agent in the HTTP request
user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
values = {'name': 'Michael Foord',
          'location': 'Northampton',
          'language': 'Python' }
headers = {'User-Agent': user_agent}
data = urllib.urlencode(values)
#
for word in wordList:
    theAddress='https://www.merriam-webster.com/dictionary/%s'%(word.encode('utf-8'))
    req=urllib2.Request(theAddress,data,headers)
    sauce=urllib2.urlopen(req).read()
    soup=bs.BeautifulSoup(sauce,'lxml')
    nav=soup.nav
    for div in soup.find_all('ol',class_='definition-list no-count'):
        print div.text.encode('utf-8')
#for url in nav.find_all('a'):
#    print(url.get('href')

# wordList=[acerbic,aggrandize,alchemy,amenable,anachronism]
#for word in wordList:
#    theAddress='https://www.merriam-webster.com/dictionary/'+word
#    sauce=urllib.requst.urlopen(theAddress).read()
#    soup=bs.BeautifulSoup(sauce,'lxml')
#    
    
#body=soup.body
#for paragraph in body.find_all('p'):
#    print(paragraph.text)


f.close()
raw_input('Press any key to exit')