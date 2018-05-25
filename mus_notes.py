

import time, sys
import pysynth_b as psb
from pygame import mixer
import winsound

w_notes =["a","a#","b","b","c#","d","d#","e","f","f#","g","g#","a","a#","b" ,"c" ,"c#","d","d#" ,"e","f","f#","g","g#" ]
i_notes= ["S","r","R","g","G","M","m","P","d","D","n","N","S'"]



duration =4
scale ='c#'
sargam ='S'  #R G M P D N S
w_sargam=((w_notes[i_notes.index(c)+w_notes.index(scale)],duration) for c in sargam.split())

print(tuple( w_sargam))

w_sargam=(('c4', 161),)

psb.make_wav(w_sargam, fn="d://test.wav", leg_stac = .7, bpm = 280)  #tuple( w_sargam)
winsound.PlaySound('d:/test.wav', winsound.SND_ASYNC)

#time.sleep(12)
lines = sys.stdin.readlines()
