

import time, sys
import pysynth_b as psb
from pygame import mixer
import winsound


w_notes =["a","a#","b","b","c#","d","d#","e","f","f#","g","g#","a","a#","b" ,"c" ,"c#","d","d#" ,"e","f","f#","g","g#" ]
i_notes= ["S","r","R","g","G","M","m","P","d","D","n","N","S'"]


def get_note(c,scl):
    ind=i_notes.index(c)+w_notes.index(scl)
    oct=4 if(ind+1) <=12 else 5
    return w_notes[ind]+str(oct)


ocatv = 12
duration =2
scale ='c#'
sargam ='S R G M P D N'
w_sargam=tuple((get_note(c,scale),duration) for c in sargam.split())

print( w_sargam)



psb.make_wav(w_sargam, fn="d://test.wav", leg_stac = 1, bpm = 200)  #tuple( w_sargam)
winsound.PlaySound('d:/test.wav', winsound.SND_ASYNC)


