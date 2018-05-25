

import time, sys
import pysynth_p as psb
from pygame import mixer
import winsound

w_notes =["c","c#","d","d#","e","f","f#","g","g#","a","a#","b" ]
i_notes= ["S","r","R","g","G","M","m","P","d","D","n","N"]

def default_octav(c) :
    if("'" in c): #uppper octav 
        return 4
    elif ("," in c ):
        return 2 # lower ocatav 
    else :
        return 3 # mid ocatav

def get_note(c,scl):
    ind=i_notes.index(c.replace("'","").replace(",",""))+w_notes.index(scl)
    oct= default_octav(c) +(int((ind+1)/12)+(((ind+1)%12) >0 if 1 else 0))
    rindex=ind if(ind<12) else ind%12 
    rs= w_notes[rindex]+str(oct)   
   # print (ind, c, i_notes.index(c.replace("'","").replace(",","")),oct,rs)  
    return rs


ocatv = 12
duration =2
scale ='c#'
sargam ="S r G M P D n S' S' n D P M G r S"
w_sargam=tuple((get_note(c,scale),duration) for c in sargam.split())

print( w_sargam)

psb.make_wav(w_sargam, fn="d://test.wav",  bpm = 200)  #tuple( w_sargam)
winsound.PlaySound('d:/test.wav', winsound.SND_ASYNC)

#C#    D#    F      F#     G#    a#    C      C#
